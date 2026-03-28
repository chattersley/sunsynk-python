# PlantInfoProduct

Energy provider product in plant info response


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `direction`                                 | *Optional[int]*                             | :heavy_minus_sign:                          | 1 = export, 0 = import                      |
| `rates_threshold`                           | *Optional[float]*                           | :heavy_minus_sign:                          | N/A                                         |
| `limit_soc`                                 | *OptionalNullable[int]*                     | :heavy_minus_sign:                          | State of charge limit (%). Null for export. |
| `provider`                                  | *Optional[int]*                             | :heavy_minus_sign:                          | Energy provider ID                          |
| `region_id`                                 | *Optional[int]*                             | :heavy_minus_sign:                          | Region ID                                   |