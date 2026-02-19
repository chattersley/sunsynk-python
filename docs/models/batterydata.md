# BatteryData


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `etoday_chg`                              | *Optional[float]*                         | :heavy_minus_sign:                        | Battery charge energy today (kWh)         |
| `etoday_dischg`                           | *Optional[float]*                         | :heavy_minus_sign:                        | Battery discharge energy today (kWh)      |
| `emonth_chg`                              | *Optional[float]*                         | :heavy_minus_sign:                        | Battery charge energy this month (kWh)    |
| `emonth_dischg`                           | *Optional[float]*                         | :heavy_minus_sign:                        | Battery discharge energy this month (kWh) |
| `eyear_chg`                               | *Optional[float]*                         | :heavy_minus_sign:                        | Battery charge energy this year (kWh)     |
| `eyear_dischg`                            | *Optional[float]*                         | :heavy_minus_sign:                        | Battery discharge energy this year (kWh)  |
| `etotal_chg`                              | *Optional[float]*                         | :heavy_minus_sign:                        | Total battery charge energy (kWh)         |
| `etotal_dischg`                           | *Optional[float]*                         | :heavy_minus_sign:                        | Total battery discharge energy (kWh)      |
| `type`                                    | *Optional[str]*                           | :heavy_minus_sign:                        | Battery type                              |
| `power`                                   | *Optional[float]*                         | :heavy_minus_sign:                        | Battery power (kW)                        |
| `capacity`                                | *Optional[float]*                         | :heavy_minus_sign:                        | Battery capacity (kWh)                    |
| `correct_cap`                             | *Optional[float]*                         | :heavy_minus_sign:                        | Corrected capacity (kWh)                  |
| `current`                                 | *Optional[float]*                         | :heavy_minus_sign:                        | Battery current (A)                       |
| `voltage`                                 | *Optional[float]*                         | :heavy_minus_sign:                        | Battery voltage (V)                       |
| `temp`                                    | *Optional[float]*                         | :heavy_minus_sign:                        | Battery temperature (°C)                  |
| `soc`                                     | *Optional[float]*                         | :heavy_minus_sign:                        | State of charge (%)                       |
| `charge_volt`                             | *Optional[float]*                         | :heavy_minus_sign:                        | Charge voltage (V)                        |
| `discharge_volt`                          | *Optional[float]*                         | :heavy_minus_sign:                        | Discharge voltage (V)                     |
| `charge_current_limit`                    | *Optional[float]*                         | :heavy_minus_sign:                        | Charge current limit (A)                  |
| `discharge_current_limit`                 | *Optional[float]*                         | :heavy_minus_sign:                        | Discharge current limit (A)               |
| `max_charge_current_limit`                | *Optional[float]*                         | :heavy_minus_sign:                        | Maximum charge current limit (A)          |
| `max_discharge_current_limit`             | *Optional[float]*                         | :heavy_minus_sign:                        | Maximum discharge current limit (A)       |
| `status`                                  | *Optional[str]*                           | :heavy_minus_sign:                        | Battery status                            |
| `battery_soc1`                            | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 1 state of charge (%)             |
| `battery_current1`                        | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 1 current (A)                     |
| `battery_volt1`                           | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 1 voltage (V)                     |
| `battery_power1`                          | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 1 power (kW)                      |
| `battery_temp1`                           | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 1 temperature (°C)                |
| `battery_status2`                         | *Optional[str]*                           | :heavy_minus_sign:                        | Battery 2 status                          |
| `battery_soc2`                            | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 2 state of charge (%)             |
| `battery_current2`                        | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 2 current (A)                     |
| `battery_volt2`                           | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 2 voltage (V)                     |
| `battery_power2`                          | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 2 power (kW)                      |
| `battery_temp2`                           | *Optional[float]*                         | :heavy_minus_sign:                        | Battery 2 temperature (°C)                |
| `number_of_batteries`                     | *Optional[int]*                           | :heavy_minus_sign:                        | Number of batteries                       |
| `batt1_factory`                           | *Optional[str]*                           | :heavy_minus_sign:                        | Battery 1 factory                         |
| `batt2_factory`                           | *Optional[str]*                           | :heavy_minus_sign:                        | Battery 2 factory                         |