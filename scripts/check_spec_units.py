#!/usr/bin/env python3
"""Regression check for sunsynk-openapi.json unit annotations.

Prevents re-introducing the bugs fixed in spec v1.2.0:
    - power fields must not claim (kW) — the API returns watts
    - energy counters must say (kWh)
    - Vip.volt / Vip.current must be typed string (the API returns stringified numbers)

Invoked by .github/workflows/validate-spec.yaml. Exit non-zero on failure.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SPEC = Path(__file__).resolve().parent.parent / "sunsynk-openapi.json"

POWER_FIELD_HINTS = ("power", "pac", "pInv", "ppv", "limiterTotalPower")
ENERGY_FIELD_HINTS = ("etoday", "etotal", "emonth", "eyear", "dailyUsed", "totalUsed")

NAMEPLATE_ALLOWLIST = {
    ("PlantInfo", "totalPower"),
    ("PlantInfoRealtime", "totalPower"),
}


def iter_fields(schemas: dict):
    for schema_name, schema in schemas.items():
        for field_name, field in (schema.get("properties") or {}).items():
            yield schema_name, field_name, field


def main() -> int:
    spec = json.loads(SPEC.read_text())
    schemas = spec["components"]["schemas"]
    errors: list[str] = []

    for schema_name, field_name, field in iter_fields(schemas):
        desc = (field.get("description") or "").lower()

        is_power = any(hint.lower() in field_name.lower() for hint in POWER_FIELD_HINTS)
        if is_power and "(kw)" in desc:
            if (schema_name, field_name) in NAMEPLATE_ALLOWLIST:
                continue
            errors.append(
                f"{schema_name}.{field_name}: power field says (kW) — API returns watts. "
                f"Description: {field.get('description')!r}"
            )

        is_energy = any(hint.lower() in field_name.lower() for hint in ENERGY_FIELD_HINTS)
        if is_energy and desc and "(kwh)" not in desc and "(w)" in desc:
            errors.append(
                f"{schema_name}.{field_name}: energy field annotated (W), should be (kWh). "
                f"Description: {field.get('description')!r}"
            )

    vip = schemas.get("Vip", {}).get("properties", {})
    if vip.get("volt", {}).get("type") != "string":
        errors.append("Vip.volt must be type 'string' — API returns stringified numbers.")
    if vip.get("current", {}).get("type") != "string":
        errors.append("Vip.current must be type 'string' — API returns stringified numbers.")
    if "voltage" in vip:
        errors.append("Vip.voltage is a leftover field name — rename to 'volt' to match the API.")

    if errors:
        print("Spec unit check failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"Spec unit check passed ({len(list(iter_fields(schemas)))} fields scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
