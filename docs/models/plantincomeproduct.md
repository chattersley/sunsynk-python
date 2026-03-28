# PlantIncomeProduct

Energy provider product configuration for Live Price (UK only)


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `direction`                                                    | *Optional[int]*                                                | :heavy_minus_sign:                                             | Energy direction: 1 = export, 0 = import                       |
| `rates_threshold`                                              | [Optional[models.RatesThreshold]](../models/ratesthreshold.md) | :heavy_minus_sign:                                             | Rate threshold value                                           |
| `provider`                                                     | *Optional[int]*                                                | :heavy_minus_sign:                                             | Energy provider ID                                             |
| `limit_soc`                                                    | *OptionalNullable[int]*                                        | :heavy_minus_sign:                                             | State of charge limit (%). Null for export direction.          |
| `region_id`                                                    | *Optional[int]*                                                | :heavy_minus_sign:                                             | Region ID for the energy provider                              |