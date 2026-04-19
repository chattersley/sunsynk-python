# Plan: fix unit annotations in `sunsynk-openapi.json` and add CI/release

## Context

The root-level `sunsynk-openapi.json` is the authored source of truth for
the SunSynk Power View API spec. Speakeasy consumes it (per
`.speakeasy/workflow.yaml`) to generate the Python SDK under `src/` and
the Markdown docs under `docs/`.

Investigating issue #1 on `sunsynk-home-assistant` (values 1,000× too
large) against the reporter's live Home Assistant instance proved that
the spec's power-field unit annotations are wrong:

- The plant-flow endpoint declared `W` in the integration and shows
  `pv_power = 521 W` for a real-time PV output.
- The inverter-realtime endpoint declared `kW` in the integration, relying
  on the spec's `"Current power (kW)"` docstring, and shows `521` — with
  a unit label of `kW`.

Both values are the same raw `521`, which the plant sensor correctly
interprets as **watts**. The spec is therefore 1,000× off for every power
field. The SDK, the HA integration, and any third party using this spec
will all inherit that mistake.

35 description strings in `sunsynk-openapi.json` contain `kW` or `kWh`.
Most `kWh` occurrences are genuinely energy counters (`etoday`, `etotal`,
`etodayChg`, etc.) and match reality. The `kW` occurrences (13) are the
ones to fix.

## Scope — spec changes

### 1. Power fields (wrong unit)

Rewrite 13 description strings from `(kW)` to `(W)`. Also add a
SunSynk-shaped `x-unit` extension on each so SDK generators can emit
stronger types if they wish.

| Schema.field | Current | Proposed |
|---|---|---|
| `Vip.power` | `Power (kW)` | `Power (W)` |
| `PvIv.ppv` | `PV power (kW)` | `PV power (W)` |
| `InputData.pac` | `Current power (kW)` | `Current power (W)` |
| `OutputData.pInv` | `Inverter power (kW)` | `Inverter power (W)` |
| `OutputData.pac` | `Output power (kW)` | `Output power (W)` |
| `GridData.pac` | `Grid power (kW)` | `Grid power (W)` |
| `GridData.limiterTotalPower` | `Total limiter power (kW)` | `Total limiter power (W)` |
| `BatteryData.power` | `Battery power (kW)` | `Battery power (W)` |
| `BatteryData.batteryPower1` | `Battery 1 power (kW)` | `Battery 1 power (W)` |
| `BatteryData.batteryPower2` | `Battery 2 power (kW)` | `Battery 2 power (W)` |
| `PlantInfo.totalPower` | `Total power capacity (kW)` | `Total power capacity (kW)` — **keep** (verified: returned `5.5` for a 5.5 kWp inverter nameplate) |
| `PlantInfoRealtime.totalPower` | `Total power capacity (kW)` | `Total power capacity (kW)` — **keep** (verified: same nameplate 5.5) |
| `Plant.pac` | `Current power (kW)` | `Current power (W)` — **fix** (verified: returned `2172` alongside `InputData.pac=2172` — same raw watt value) |
| `PlantInfoRealtime.pac` | `(no annotation)` | add `Current power (W)` — verified `2172` |

### 2. Battery capacity (Ah vs kWh)

`BatteryData.capacity` and `BatteryData.correctCap` are labelled `(kWh)`.
Evidence from the reporter's inverter: `correctCap = 100`, which matches
the nameplate Ah of a typical 48 V lithium stack, not kWh (5.12 kWh at
51.2 V × 100 Ah = 5120 Wh → 5.12 kWh, which the API would report as ~5.1
not 100).

Proposed change:

- `BatteryData.capacity` → `Battery capacity (Ah)`
- `BatteryData.correctCap` → `Corrected capacity (Ah)`

### 3. Keep as-is (verified correct)

All `kWh` energy counters (`etoday*`, `etotal*`, `emonth*`, `eyear*`,
`etodayFrom/To`, `etotalFrom/To`, etc.). These read plausibly in kWh on
the live instance (grid_total_import = 31,366.7 kWh over a multi-year
install).

### 4. Bonus findings from verification (2026-04-19 live dump)

Surfaced while running the one-shot verification script; fold into the
same spec edit so the release is coherent.

- **`LoadData.total_power`** — no annotation. Live value `0` when idle.
  Shape matches the other realtime power fields; should be annotated
  `Total load power (W)`.
- **`LoadData.daily_used`** — no annotation. Live value `0` when idle
  (counter). Should be `Daily energy used (kWh)`.
- **`Vip.volt` / `Vip.current`** — spec declares `type: number` but the
  API returns **strings** (e.g. `'245.5'`). This is a type-fidelity bug,
  not a unit bug, and widens the scope slightly. Options:
    a. Change the spec type to `string` and document why.
    b. Use `oneOf: [{type: number}, {type: string}]` to reflect reality.
    c. Leave the spec as `number` and file a vendor bug.
  Prefer (a) — matches observed behaviour, smallest blast radius on
  the generated SDK. Mention in release notes that `Vip.volt/current`
  are now typed as string.

## Open questions — resolved by verification (2026-04-19)

All three originally-open questions were resolved by running
`/tmp/verify_units.py` against the reporter's live instance:

1. **`Plant.pac` / `PlantInfoRealtime.totalPower` / `pac`** — plant
   summary reports power in **watts**. `Plant.pac` and the plant's
   `InputData.pac` both returned the identical raw value `2172` on the
   same tick. `PlantInfo.totalPower` returned `5.5` — genuinely kW
   (nameplate). ✅ Fix `Plant.pac`, keep `totalPower` as kW.
2. **`BatteryData.capacity` / `correctCap`** — both returned `100` for
   a 5.12 kWh (100 Ah × 51.2 V) lithium stack. Confirmed Ah, not kWh.
   ✅ Relabel to Ah.
3. **`Vip.power`** — returned live values consistent with the parent
   endpoint's `pac` (e.g. `GridData.pac = -4688` W, `vip[0].power =
   -1563` W — same units, summed across phases). ✅ Watts.

See "Bonus findings" above for issues surfaced during verification that
were not on the original list.

## Scope — CI / release

Two independent workflows to add under `.github/workflows/`. Neither
exists today (only `.github/copilot/skills/` is present; no `workflows/`
directory at all).

### Workflow A — spec validation on PRs

`.github/workflows/validate-spec.yaml`:

- Trigger: `pull_request` touching `sunsynk-openapi.json` or
  `.speakeasy/**`.
- Steps:
  1. Checkout.
  2. `npx @redocly/cli lint sunsynk-openapi.json` — catches malformed
     OpenAPI, broken `$ref`s, inconsistent types. Redocly is the
     industry-standard linter, Apache 2.0, no login.
  3. `npx @apidevtools/swagger-cli validate sunsynk-openapi.json` — a
     second opinion against the OpenAPI 3.0 schema.
  4. Optional: `uv run pytest tests/spec/` — a tiny pytest file (added
     with this work) that asserts no `(kW)` appears in a power-field
     description and no `(Wh)` appears in an energy-field description.
     Prevents regressions from future hand-edits.

Reason for Redocly + swagger-cli together: they catch different classes
of error; redocly is opinionated (will warn on missing tags/examples),
swagger-cli is purely schema-valid. Start with both and prune later if
one is redundant.

### Workflow B — spec release on tag

`.github/workflows/release-spec.yaml`:

- Trigger: `push` on tags matching `spec-v*` (keeps spec versioning
  independent of the Python SDK's `v*` tags).
- Steps:
  1. Checkout.
  2. Validate (same steps as Workflow A — a tag shouldn't ship an
     invalid spec even if main somehow drifted).
  3. Convert JSON → YAML for consumers that prefer YAML:
     `yq -p=json -o=yaml sunsynk-openapi.json > sunsynk-openapi.yaml`.
  4. `gh release create "$GITHUB_REF_NAME" --generate-notes \
        sunsynk-openapi.json sunsynk-openapi.yaml \
        .speakeasy/out.openapi.yaml`.
  5. Optional (stretch): publish to a GitHub Pages site at
     `chattersley.github.io/sunsynk-python/openapi.json` so tooling can
     fetch a stable URL without needing a release-asset download. Low
     priority.

Deliberately NOT in Workflow B: re-running Speakeasy SDK generation. The
Speakeasy GitHub App (referenced in the README) already handles SDK
regen on spec changes when configured properly; we don't want two
generators racing. If the Speakeasy app isn't set up yet, that becomes a
separate setup task, not part of this plan.

### Workflow C — Python SDK publish (optional)

The `scripts/publish.sh` already does `uv build && uv publish --token
$PYPI_TOKEN`. Wrapping that in a workflow that triggers on `v*` tags is
one file:

```yaml
name: Publish Python SDK
on:
  push:
    tags: ["v*"]
jobs:
  pypi:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv build
      - run: uv publish --token ${{ secrets.PYPI_TOKEN }}
```

Include this or not depending on whether Speakeasy is already handling
publish. Ask first.

## Versioning strategy

Bumping only the description strings does not change the wire contract,
so technically it's a patch. But it does rename a unit which consumers
may depend on — recommend treating it as **minor** (`1.1.0` → `1.2.0`)
to signal "semantic change, interpret fields differently". Cut the first
release immediately after merging:

1. Edit `info.version: 1.1.0` → `1.2.0` in the spec.
2. Tag `spec-v1.2.0`.
3. GitHub release auto-created by Workflow B.
4. Separately, Speakeasy regenerates the SDK with new docstrings;
   version-bump the SDK to match.

## Consumer impact

Downstream projects and their expected response to the spec fix:

- **`sunsynk-home-assistant`** — currently broken (issue #1). Needs
  parallel fix (analysis doc already on the `issue-analysis` branch).
  Doesn't consume the spec directly — it consumes the SDK — so will
  benefit automatically once the SDK is regenerated with the new
  docstrings.
- **`energy-pilot` (Joule Genie)** — doesn't use the SDK; uses a
  hand-written mapper that already treats these fields as watts. No
  change needed (verified — see prior conversation turn).
- **Anyone else using `sunsynk_api_client` from PyPI** — will see
  corrected docstrings on next SDK release and may notice their
  dashboards are wrong. Release notes should call it out loudly.

## Suggested landing order

1. ~~Run the one-shot verification script against the reporter's account.~~ ✅ done
2. ~~Fill in the open questions above.~~ ✅ done
3. Edit `sunsynk-openapi.json` (one commit — all unit + annotation + Vip-type fixes together).
4. Re-run Speakeasy locally to regenerate `.speakeasy/out.openapi.yaml`,
   `src/sunsynk_api_client/models/**`, and `docs/models/**`. Commit the
   regenerated artefacts separately so the first diff is reviewable.
5. Add Workflow A and the pytest spec-regression test.
6. Add Workflow B (release).
7. Bump `info.version` to `1.2.0` and cut `spec-v1.2.0`.
8. Optionally add Workflow C for Python SDK publish.

Each step is independently reviewable and revertible.

## Challenges and alternatives considered

- **Keep `kW` and scale in the SDK?** Rejected. The SDK is generated by
  a third party tool with no unit-aware scaling hooks. Fixing the source
  spec is simpler and more honest.
- **Add an `x-unit` extension and leave descriptions alone?**
  Rejected — the description is the only thing humans see; an
  extension is invisible in `docs/models/*.md` output.
- **Ship as a patch (1.1.1)?** Weakly rejected. Minor communicates
  semantic change better, even if the schema types are unchanged.
- **Skip Workflow B and ask users to pull from `main`?** Fine for
  initial release, but consumers like Joule Genie prefer a pinned
  version. A GitHub release with a stable asset URL is a 20-line
  workflow that removes a whole class of "which version did I grab"
  questions.

## What this plan does not cover

- Re-generating the Speakeasy SDK's type-safe unit wrappers
  (e.g. `Watts` vs `Kilowatts`). Speakeasy doesn't support that today;
  revisit if the generator adds it.
- Fixing the `sunsynk-home-assistant` integration (tracked separately
  on the `issue-analysis` branch in that repo).
- Upstream contribution back to SunSynk — the spec was hand-written
  from Node-RED flow observation; there is no upstream.
