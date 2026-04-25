"""Tests for InverterSettingsSet model — battery cap fields added in 0.4.1."""

from __future__ import annotations

import json

import pytest

from sunsynk_api_client.models.invertersettingsset import InverterSettingsSet


class TestBatteryCapFields:
    """battery_restart_cap and battery_shutdown_cap serialise with camelCase aliases."""

    def test_battery_restart_cap_serialises(self) -> None:
        m = InverterSettingsSet(battery_restart_cap="15")
        payload = json.loads(m.model_dump_json(by_alias=True, exclude_none=True))
        assert payload == {"batteryRestartCap": "15"}

    def test_battery_shutdown_cap_serialises(self) -> None:
        m = InverterSettingsSet(battery_shutdown_cap="10")
        payload = json.loads(m.model_dump_json(by_alias=True, exclude_none=True))
        assert payload == {"batteryShutdownCap": "10"}

    def test_both_caps_and_max_charge_together(self) -> None:
        m = InverterSettingsSet(
            battery_restart_cap="15",
            battery_shutdown_cap="10",
            battery_max_current_charge="50",
        )
        payload = json.loads(m.model_dump_json(by_alias=True, exclude_none=True))
        assert payload["batteryRestartCap"] == "15"
        assert payload["batteryShutdownCap"] == "10"
        assert payload["batteryMaxCurrentCharge"] == "50"

    def test_none_fields_excluded(self) -> None:
        m = InverterSettingsSet(battery_restart_cap="20")
        payload = json.loads(m.model_dump_json(by_alias=True, exclude_none=True))
        assert "batteryShutdownCap" not in payload

    def test_typed_dict_accepts_new_keys(self) -> None:
        from sunsynk_api_client.models.invertersettingsset import InverterSettingsSetTypedDict
        d: InverterSettingsSetTypedDict = {
            "battery_restart_cap": "15",
            "battery_shutdown_cap": "10",
        }
        assert d["battery_restart_cap"] == "15"
        assert d["battery_shutdown_cap"] == "10"

    def test_set_inverter_settings_async_accepts_new_params(self) -> None:
        """set_inverter_settings_async signature must accept the new fields."""
        import inspect
        from sunsynk_api_client.settings import Settings

        sig = inspect.signature(Settings.set_inverter_settings_async)
        assert "battery_restart_cap" in sig.parameters
        assert "battery_shutdown_cap" in sig.parameters

    def test_set_inverter_settings_accepts_new_params(self) -> None:
        """Sync set_inverter_settings signature must accept the new fields."""
        import inspect
        from sunsynk_api_client.settings import Settings

        sig = inspect.signature(Settings.set_inverter_settings)
        assert "battery_restart_cap" in sig.parameters
        assert "battery_shutdown_cap" in sig.parameters
