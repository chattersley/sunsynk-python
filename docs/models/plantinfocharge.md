# PlantInfoCharge

A pricing charge entry returned in the plant info response


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `start_range`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Start time (HH:MM)                                                   |
| `end_range`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | End time (HH:MM)                                                     |
| `price`                                                              | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Price per unit                                                       |
| `type`                                                               | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Pricing type: 1 = Constant, 2 = Time of Use, 3 = Live Price          |
| `station_id`                                                         | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Plant/station ID                                                     |
| `create_at`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `status`                                                             | [Optional[models.Status]](../models/status.md)                       | :heavy_minus_sign:                                                   | Energy direction for this charge                                     |