# InverterData

## Overview

Real-time inverter data endpoints (battery, grid, load, generation)

### Available Operations

* [get_inverter_input](#get_inverter_input) - Get inverter input data
* [get_inverter_output](#get_inverter_output) - Get inverter output data
* [get_battery_realtime](#get_battery_realtime) - Get battery realtime data
* [get_grid_realtime](#get_grid_realtime) - Get grid realtime data
* [get_load_realtime](#get_load_realtime) - Get load realtime data
* [get_gen_realtime](#get_gen_realtime) - Get generation realtime data
* [get_inverter_daily_output](#get_inverter_daily_output) - Get inverter daily output

## get_inverter_input

Retrieves real-time input data (PV) for a specific inverter

### Example Usage

<!-- UsageSnippet language="python" operationID="getInverterInput" method="get" path="/api/v1/inverter/{sn}/realtime/input" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.inverter_data.get_inverter_input(sn="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sn`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InputResponse](../../models/inputresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## get_inverter_output

Retrieves real-time output data for a specific inverter

### Example Usage

<!-- UsageSnippet language="python" operationID="getInverterOutput" method="get" path="/api/v1/inverter/{sn}/realtime/output" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.inverter_data.get_inverter_output(sn="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sn`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OutputResponse](../../models/outputresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## get_battery_realtime

Retrieves real-time battery information for a specific inverter

### Example Usage

<!-- UsageSnippet language="python" operationID="getBatteryRealtime" method="get" path="/api/v1/inverter/battery/{sn}/realtime" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.inverter_data.get_battery_realtime(sn="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sn`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `lan`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BatteryResponse](../../models/batteryresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## get_grid_realtime

Retrieves real-time grid information for a specific inverter

### Example Usage

<!-- UsageSnippet language="python" operationID="getGridRealtime" method="get" path="/api/v1/inverter/grid/{sn}/realtime" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.inverter_data.get_grid_realtime(sn="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sn`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GridResponse](../../models/gridresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## get_load_realtime

Retrieves real-time load information for a specific inverter

### Example Usage

<!-- UsageSnippet language="python" operationID="getLoadRealtime" method="get" path="/api/v1/inverter/load/{sn}/realtime" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.inverter_data.get_load_realtime(sn="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sn`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetLoadRealtimeResponse](../../models/getloadrealtimeresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## get_gen_realtime

Retrieves real-time solar generation information for a specific inverter

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenRealtime" method="get" path="/api/v1/inverter/gen/{sn}/realtime" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.inverter_data.get_gen_realtime(sn="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sn`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetGenRealtimeResponse](../../models/getgenrealtimeresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## get_inverter_daily_output

Retrieves daily output statistics for a specific inverter

### Example Usage

<!-- UsageSnippet language="python" operationID="getInverterDailyOutput" method="get" path="/api/v1/inverter/{sn}/output/day" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.inverter_data.get_inverter_daily_output(sn="<value>", lan="en")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `sn`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `lan`                                                                        | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `date_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | N/A                                                                          |
| `column`                                                                     | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.GetInverterDailyOutputResponse](../../models/getinverterdailyoutputresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |