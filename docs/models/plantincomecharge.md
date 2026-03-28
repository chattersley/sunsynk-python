# PlantIncomeCharge


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `price`                                                                     | [Optional[models.Price]](../models/price.md)                                | :heavy_minus_sign:                                                          | Price per unit of energy. String for types 1 and 2, integer (0) for type 3. |
| `type`                                                                      | [Optional[models.Type]](../models/type.md)                                  | :heavy_minus_sign:                                                          | Pricing type: 1 = Constant Price, 2 = Time of Use, 3 = Live Price (UK only) |
| `start_range`                                                               | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Start time (HH:MM). Empty string for Live Price.                            |
| `end_range`                                                                 | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | End time (HH:MM). Empty string for Live Price.                              |