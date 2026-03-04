# Events

## Overview

Endpoints for system events

### Available Operations

* [get_events](#get_events) - Get events

## get_events

Retrieves system events (warnings, alarms, etc.)

### Example Usage

<!-- UsageSnippet language="python" operationID="getEvents" method="get" path="/api/v1/events" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.events.get_events(type_=108693, page=1, limit=50, lan="en")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `type`                                                                       | *int*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `page`                                                                       | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `limit`                                                                      | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `lan`                                                                        | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `sdate`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | N/A                                                                          |
| `edate`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | N/A                                                                          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.GetEventsResponse](../../models/geteventsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |