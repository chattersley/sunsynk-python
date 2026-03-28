# Plants

## Overview

Endpoints for retrieving plant and energy flow data

### Available Operations

* [get_plants](#get_plants) - Get list of plants
* [get_plant_flow](#get_plant_flow) - Get plant energy flow data
* [set_plant_income](#set_plant_income) - Set plant income pricing

## get_plants

Retrieves a list of all plants associated with the account

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlants" method="get" path="/api/v1/plants" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.plants.get_plants(page=1, limit=100)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlantsResponse](../../models/plantsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## get_plant_flow

Retrieves real-time energy flow data for a specific plant

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlantFlow" method="get" path="/api/v1/plant/energy/{plantId}/flow" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.plants.get_plant_flow(plant_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `plant_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlantFlowResponse](../../models/plantflowresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## set_plant_income

Configures the electricity pricing model for a plant. Supports three pricing types: Constant Price (type 1), Time of Use (type 2), and Live Price (type 3, UK only). Time of Use allows a maximum of 6 time slots and must have one entry starting at 00:00 and one ending at 24:00.

### Example Usage: constantPrice

<!-- UsageSnippet language="python" operationID="setPlantIncome" method="post" path="/api/v1/plant/{plantId}/income" example="constantPrice" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.plants.set_plant_income(plant_id="<id>", id="345964", currency=366, invest=10730.12, charges=[
        {
            "price": "27",
            "type": "1",
            "start_range": "00:00",
            "end_range": "24:00",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: livePrice

<!-- UsageSnippet language="python" operationID="setPlantIncome" method="post" path="/api/v1/plant/{plantId}/income" example="livePrice" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.plants.set_plant_income(plant_id="<id>", id="345964", currency=366, invest=10730.12, charges=[
        {
            "price": 0,
            "type": "3",
            "start_range": "",
            "end_range": "",
        },
    ], products=[
        {
            "direction": 1,
            "rates_threshold": "25",
            "provider": 1,
            "limit_soc": None,
            "region_id": 8,
        },
        {
            "direction": 0,
            "rates_threshold": 30,
            "provider": 1,
            "limit_soc": 20,
            "region_id": 8,
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: timeOfUse

<!-- UsageSnippet language="python" operationID="setPlantIncome" method="post" path="/api/v1/plant/{plantId}/income" example="timeOfUse" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.plants.set_plant_income(plant_id="<id>", id="345964", currency=366, invest=10730.12, charges=[
        {
            "price": "83",
            "type": 2,
            "start_range": "00:00",
            "end_range": "03:30",
        },
        {
            "price": "100",
            "type": 2,
            "start_range": "03:30",
            "end_range": "05:00",
        },
        {
            "price": "20",
            "type": 2,
            "start_range": "05:00",
            "end_range": "07:30",
        },
        {
            "price": "20",
            "type": 2,
            "start_range": "07:30",
            "end_range": "13:00",
        },
        {
            "price": "100",
            "type": 2,
            "start_range": "13:00",
            "end_range": "16:30",
        },
        {
            "price": "20",
            "type": 2,
            "start_range": "16:30",
            "end_range": "24:00",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `plant_id`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                         |
| `id`                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                          | Plant ID                                                                                                                                                                                                                                    |
| `currency`                                                                                                                                                                                                                                  | *int*                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                          | Currency code                                                                                                                                                                                                                               |
| `invest`                                                                                                                                                                                                                                    | *float*                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                          | Total investment amount                                                                                                                                                                                                                     |
| `charges`                                                                                                                                                                                                                                   | List[[models.PlantIncomeCharge](../../models/plantincomecharge.md)]                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                          | Pricing entries. For Constant Price (type 1): single entry covering 00:00–24:00. For Time of Use (type 2): up to 6 time slots, must start at 00:00 and end at 24:00. For Live Price (type 3, UK only): single entry with empty time ranges. |
| `products`                                                                                                                                                                                                                                  | List[[models.PlantIncomeProduct](../../models/plantincomeproduct.md)]                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                          | Energy provider products. Only used with Live Price (type 3, UK only).                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                         |

### Response

**[models.SetPlantIncomeResponse](../../models/setplantincomeresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |