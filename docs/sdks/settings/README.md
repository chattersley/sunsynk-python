# Settings

## Overview

Endpoints for reading and writing inverter settings

### Available Operations

* [read_inverter_settings](#read_inverter_settings) - Read inverter settings
* [set_inverter_settings](#set_inverter_settings) - Set inverter settings

## read_inverter_settings

Retrieves the configuration settings for a specific inverter

### Example Usage

<!-- UsageSnippet language="python" operationID="readInverterSettings" method="get" path="/api/v1/common/setting/{sn}/read" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.settings.read_inverter_settings(sn="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sn`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InverterSettingsResponse](../../models/invertersettingsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## set_inverter_settings

Updates the configuration settings for a specific inverter. Accepts partial requests — only the fields included in the request body will be updated, all other settings remain unchanged.

### Example Usage: full

<!-- UsageSnippet language="python" operationID="setInverterSettings" method="post" path="/api/v1/common/setting/{sn}/set" example="full" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.settings.set_inverter_settings(sn_param="<value>", sn="2210085392", safety_type="0", batt_mode="-1", solar_sell="1", pv_max_limit="5000", energy_mode="1", peak_and_vallery="1", sys_work_mode="2", sell_time1="08:00", sell_time2="08:30", sell_time3="05:00", sell_time4="10:00", sell_time5="12:30", sell_time6="16:00", sell_time1_pac="5000", sell_time2_pac="5000", sell_time3_pac="5000", sell_time4_pac="5000", sell_time5_pac="5000", sell_time6_pac="5000", cap1="20", cap2="20", cap3="20", cap4="40", cap5="100", cap6="20", sell_time1_volt="41", sell_time2_volt="41", sell_time3_volt="49", sell_time4_volt="49", sell_time5_volt="49", sell_time6_volt="49", zero_export_power="20", solar_max_sell_power="6500", grid_peak_shaving="0", generator_start_cap="10", battery_low_cap="35", time1on=False, time2on=False, time3on=False, time4on=True, time5on=True, time6on=False, gen_time1on=False, gen_time2on=False, gen_time3on=False, gen_time4on=False, gen_time5on=False, gen_time6on=False, monday_on=True, tuesday_on=True, wednesday_on=True, thursday_on=True, friday_on=True, saturday_on=True, sunday_on=True)

    # Handle response
    print(res)

```
### Example Usage: minimal

<!-- UsageSnippet language="python" operationID="setInverterSettings" method="post" path="/api/v1/common/setting/{sn}/set" example="minimal" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.settings.set_inverter_settings(sn_param="<value>", sell_time1="08:30", sell_time2="09:30", sell_time3="05:00", sell_time4="10:00", sell_time5="12:30", sell_time6="16:00", cap1="20", cap2="20", cap3="20", cap4="40", cap5="100", cap6="20", time1on=True, time2on=False, time3on=True, time4on=False, time5on=True, time6on=False, gen_time1on=False, gen_time2on=False, gen_time3on=False, gen_time4on=False, gen_time5on=False, gen_time6on=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sn_param`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `sn`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Inverter serial number                                              |
| `safety_type`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `batt_mode`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `solar_sell`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `pv_max_limit`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `energy_mode`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `peak_and_vallery`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sys_work_mode`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time1`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Time slot 1 start time (HH:MM)                                      |
| `sell_time2`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Time slot 2 start time (HH:MM)                                      |
| `sell_time3`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Time slot 3 start time (HH:MM)                                      |
| `sell_time4`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Time slot 4 start time (HH:MM)                                      |
| `sell_time5`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Time slot 5 start time (HH:MM)                                      |
| `sell_time6`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Time slot 6 start time (HH:MM)                                      |
| `sell_time1_pac`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time2_pac`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time3_pac`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time4_pac`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time5_pac`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time6_pac`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cap1`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Battery capacity threshold for time slot 1 (%)                      |
| `cap2`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Battery capacity threshold for time slot 2 (%)                      |
| `cap3`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Battery capacity threshold for time slot 3 (%)                      |
| `cap4`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Battery capacity threshold for time slot 4 (%)                      |
| `cap5`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Battery capacity threshold for time slot 5 (%)                      |
| `cap6`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Battery capacity threshold for time slot 6 (%)                      |
| `sell_time1_volt`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time2_volt`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time3_volt`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time4_volt`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time5_volt`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sell_time6_volt`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `zero_export_power`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `solar_max_sell_power`                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `grid_peak_shaving`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `low_volt_cross_en`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `generator_start_cap`                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `battery_low_cap`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `time1on`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable time slot 1                                                  |
| `time2on`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable time slot 2                                                  |
| `time3on`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable time slot 3                                                  |
| `time4on`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable time slot 4                                                  |
| `time5on`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable time slot 5                                                  |
| `time6on`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable time slot 6                                                  |
| `gen_time1on`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable generator time slot 1                                        |
| `gen_time2on`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable generator time slot 2                                        |
| `gen_time3on`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable generator time slot 3                                        |
| `gen_time4on`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable generator time slot 4                                        |
| `gen_time5on`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable generator time slot 5                                        |
| `gen_time6on`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable generator time slot 6                                        |
| `monday_on`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tuesday_on`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `wednesday_on`                                                      | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `thursday_on`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `friday_on`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `saturday_on`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sunday_on`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetInverterSettingsResponse](../../models/setinvertersettingsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |