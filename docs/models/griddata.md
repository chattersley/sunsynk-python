# GridData


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `vip`                                | List[[models.Vip](../models/vip.md)] | :heavy_minus_sign:                   | N/A                                  |
| `pac`                                | *Optional[float]*                    | :heavy_minus_sign:                   | Grid power (kW)                      |
| `qac`                                | *Optional[float]*                    | :heavy_minus_sign:                   | Reactive power (kVar)                |
| `fac`                                | *Optional[float]*                    | :heavy_minus_sign:                   | Grid frequency (Hz)                  |
| `pf`                                 | *Optional[float]*                    | :heavy_minus_sign:                   | Power factor                         |
| `status`                             | *Optional[str]*                      | :heavy_minus_sign:                   | Grid status                          |
| `etoday_from`                        | *Optional[float]*                    | :heavy_minus_sign:                   | Energy imported today (kWh)          |
| `etoday_to`                          | *Optional[float]*                    | :heavy_minus_sign:                   | Energy exported today (kWh)          |
| `etotal_from`                        | *Optional[float]*                    | :heavy_minus_sign:                   | Total energy imported (kWh)          |
| `etotal_to`                          | *Optional[float]*                    | :heavy_minus_sign:                   | Total energy exported (kWh)          |
| `limiter_power_arr`                  | List[*float*]                        | :heavy_minus_sign:                   | N/A                                  |
| `limiter_total_power`                | *Optional[float]*                    | :heavy_minus_sign:                   | Total limiter power (kW)             |