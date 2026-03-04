<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.authentication.post_oauth_token(username="Florencio.Stiedemann", password="yES5j6h4HZfL6Pn", grant_type="password", client_id="csp-web")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import os
from sunsynk_api_client import SunSynk

async def main():

    async with SunSynk(
        bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
    ) as sun_synk:

        res = await sun_synk.authentication.post_oauth_token_async(username="Florencio.Stiedemann", password="yES5j6h4HZfL6Pn", grant_type="password", client_id="csp-web")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->