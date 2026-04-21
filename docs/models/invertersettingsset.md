# InverterSettingsSet

Inverter settings to update. All properties are optional — only included fields will be updated. This endpoint accepts partial requests.


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `sn`                                           | *Optional[str]*                                | :heavy_minus_sign:                             | Inverter serial number                         |
| `safety_type`                                  | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `batt_mode`                                    | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `solar_sell`                                   | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `pv_max_limit`                                 | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `energy_mode`                                  | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `peak_and_vallery`                             | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sys_work_mode`                                | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time1`                                   | *Optional[str]*                                | :heavy_minus_sign:                             | Time slot 1 start time (HH:MM)                 |
| `sell_time2`                                   | *Optional[str]*                                | :heavy_minus_sign:                             | Time slot 2 start time (HH:MM)                 |
| `sell_time3`                                   | *Optional[str]*                                | :heavy_minus_sign:                             | Time slot 3 start time (HH:MM)                 |
| `sell_time4`                                   | *Optional[str]*                                | :heavy_minus_sign:                             | Time slot 4 start time (HH:MM)                 |
| `sell_time5`                                   | *Optional[str]*                                | :heavy_minus_sign:                             | Time slot 5 start time (HH:MM)                 |
| `sell_time6`                                   | *Optional[str]*                                | :heavy_minus_sign:                             | Time slot 6 start time (HH:MM)                 |
| `sell_time1_pac`                               | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time2_pac`                               | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time3_pac`                               | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time4_pac`                               | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time5_pac`                               | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time6_pac`                               | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `cap1`                                         | *Optional[str]*                                | :heavy_minus_sign:                             | Battery capacity threshold for time slot 1 (%) |
| `cap2`                                         | *Optional[str]*                                | :heavy_minus_sign:                             | Battery capacity threshold for time slot 2 (%) |
| `cap3`                                         | *Optional[str]*                                | :heavy_minus_sign:                             | Battery capacity threshold for time slot 3 (%) |
| `cap4`                                         | *Optional[str]*                                | :heavy_minus_sign:                             | Battery capacity threshold for time slot 4 (%) |
| `cap5`                                         | *Optional[str]*                                | :heavy_minus_sign:                             | Battery capacity threshold for time slot 5 (%) |
| `cap6`                                         | *Optional[str]*                                | :heavy_minus_sign:                             | Battery capacity threshold for time slot 6 (%) |
| `sell_time1_volt`                              | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time2_volt`                              | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time3_volt`                              | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time4_volt`                              | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time5_volt`                              | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `sell_time6_volt`                              | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `zero_export_power`                            | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `solar_max_sell_power`                         | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `grid_peak_shaving`                            | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `low_volt_cross_en`                            | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `generator_start_cap`                          | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `battery_low_cap`                              | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `time1on`                                      | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable time slot 1                             |
| `time2on`                                      | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable time slot 2                             |
| `time3on`                                      | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable time slot 3                             |
| `time4on`                                      | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable time slot 4                             |
| `time5on`                                      | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable time slot 5                             |
| `time6on`                                      | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable time slot 6                             |
| `gen_time1on`                                  | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable generator time slot 1                   |
| `gen_time2on`                                  | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable generator time slot 2                   |
| `gen_time3on`                                  | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable generator time slot 3                   |
| `gen_time4on`                                  | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable generator time slot 4                   |
| `gen_time5on`                                  | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable generator time slot 5                   |
| `gen_time6on`                                  | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable generator time slot 6                   |
| `sell_time1on`                                 | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable sell-to-grid for time slot 1            |
| `sell_time2on`                                 | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable sell-to-grid for time slot 2            |
| `sell_time3on`                                 | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable sell-to-grid for time slot 3            |
| `sell_time4on`                                 | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable sell-to-grid for time slot 4            |
| `sell_time5on`                                 | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable sell-to-grid for time slot 5            |
| `sell_time6on`                                 | *Optional[bool]*                               | :heavy_minus_sign:                             | Enable sell-to-grid for time slot 6            |
| `monday_on`                                    | *Optional[bool]*                               | :heavy_minus_sign:                             | N/A                                            |
| `tuesday_on`                                   | *Optional[bool]*                               | :heavy_minus_sign:                             | N/A                                            |
| `wednesday_on`                                 | *Optional[bool]*                               | :heavy_minus_sign:                             | N/A                                            |
| `thursday_on`                                  | *Optional[bool]*                               | :heavy_minus_sign:                             | N/A                                            |
| `friday_on`                                    | *Optional[bool]*                               | :heavy_minus_sign:                             | N/A                                            |
| `saturday_on`                                  | *Optional[bool]*                               | :heavy_minus_sign:                             | N/A                                            |
| `sunday_on`                                    | *Optional[bool]*                               | :heavy_minus_sign:                             | N/A                                            |