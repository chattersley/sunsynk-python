# sunsynk-api-client

Developer-friendly & type-safe Python SDK specifically catered to leverage *sunsynk-api-client* API.

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=sunsynk-api-client&utm_campaign=python)
[![License: MIT](https://img.shields.io/badge/LICENSE_//_MIT-3b5bdb?style=for-the-badge&labelColor=eff6ff)](https://opensource.org/licenses/MIT)


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/finchdean/home-assistant). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

SunSynk Power View API: API specification for SunSynk Power View (Inverter monitoring system). Combined from Node-RED flows and Python client library.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [sunsynk-api-client](#sunsynk-api-client)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+<UNSET>.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from sunsynk-api-client python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "sunsynk-api-client",
# ]
# ///

from sunsynk_api_client import SunSynk

sdk = SunSynk(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      | Environment Variable  |
| ------------- | ---- | ----------- | --------------------- |
| `bearer_auth` | http | HTTP Bearer | `SUNSYNK_BEARER_AUTH` |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.authentication.post_oauth_token(username="Florencio.Stiedemann", password="yES5j6h4HZfL6Pn", grant_type="password", client_id="csp-web")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Authentication](docs/sdks/authentication/README.md)

* [post_oauth_token](docs/sdks/authentication/README.md#post_oauth_token) - Authenticate user and obtain access token
* [get_bearer_token](docs/sdks/authentication/README.md#get_bearer_token) - Authenticate and get bearer token (new flow)
* [get_public_key](docs/sdks/authentication/README.md#get_public_key) - Get public key for password encryption

### [Events](docs/sdks/events/README.md)

* [get_events](docs/sdks/events/README.md#get_events) - Get events

### [Gateways](docs/sdks/gateways/README.md)

* [get_gateways](docs/sdks/gateways/README.md#get_gateways) - Get gateways

### [InverterData](docs/sdks/inverterdata/README.md)

* [get_inverter_input](docs/sdks/inverterdata/README.md#get_inverter_input) - Get inverter input data
* [get_inverter_output](docs/sdks/inverterdata/README.md#get_inverter_output) - Get inverter output data
* [get_battery_realtime](docs/sdks/inverterdata/README.md#get_battery_realtime) - Get battery realtime data
* [get_grid_realtime](docs/sdks/inverterdata/README.md#get_grid_realtime) - Get grid realtime data
* [get_load_realtime](docs/sdks/inverterdata/README.md#get_load_realtime) - Get load realtime data
* [get_gen_realtime](docs/sdks/inverterdata/README.md#get_gen_realtime) - Get generation realtime data
* [get_inverter_daily_output](docs/sdks/inverterdata/README.md#get_inverter_daily_output) - Get inverter daily output

### [Inverters](docs/sdks/inverters/README.md)

* [get_api_v1_inverters](docs/sdks/inverters/README.md#get_api_v1_inverters) - Get list of inverters
* [get_plant_inverters](docs/sdks/inverters/README.md#get_plant_inverters) - Get inverters for a plant

### [Notifications](docs/sdks/notifications/README.md)

* [get_messages](docs/sdks/notifications/README.md#get_messages) - Get notifications/messages

### [Plants](docs/sdks/plants/README.md)

* [get_plants](docs/sdks/plants/README.md#get_plants) - Get list of plants
* [get_plant_flow](docs/sdks/plants/README.md#get_plant_flow) - Get plant energy flow data

### [Settings](docs/sdks/settings/README.md)

* [read_inverter_settings](docs/sdks/settings/README.md#read_inverter_settings) - Read inverter settings
* [write_inverter_settings](docs/sdks/settings/README.md#write_inverter_settings) - Write inverter settings

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
from sunsynk_api_client import SunSynk
from sunsynk_api_client.utils import BackoffStrategy, RetryConfig


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.authentication.post_oauth_token(username="Florencio.Stiedemann", password="yES5j6h4HZfL6Pn", grant_type="password", client_id="csp-web",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
from sunsynk_api_client import SunSynk
from sunsynk_api_client.utils import BackoffStrategy, RetryConfig


with SunSynk(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.authentication.post_oauth_token(username="Florencio.Stiedemann", password="yES5j6h4HZfL6Pn", grant_type="password", client_id="csp-web")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SunSynkError`](./src/sunsynk_api_client/errors/sunsynkerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
import os
from sunsynk_api_client import SunSynk, errors


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:
    res = None
    try:

        res = sun_synk.authentication.post_oauth_token(username="Florencio.Stiedemann", password="yES5j6h4HZfL6Pn", grant_type="password", client_id="csp-web")

        # Handle response
        print(res)


    except errors.SunSynkError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.Error):
            print(e.data.success)  # Optional[bool]
            print(e.data.code)  # Optional[int]
            print(e.data.msg)  # Optional[str]
```

### Error Classes
**Primary error:**
* [`SunSynkError`](./src/sunsynk_api_client/errors/sunsynkerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (6)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SunSynkError`](./src/sunsynk_api_client/errors/sunsynkerror.py)**:
* [`Error`](./src/sunsynk_api_client/errors/error.py): Invalid credentials. Status code `401`. Applicable to 1 of 19 methods.*
* [`ResponseValidationError`](./src/sunsynk_api_client/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                    | Variables  | Description                   |
| --- | ------------------------- | ---------- | ----------------------------- |
| 0   | `https://pv.inteless.com` |            | Region 1 - Production server  |
| 1   | `https://api.sunsynk.net` |            | Region 2 - Alternative server |
| 2   | `https://{base_url}`      | `base_url` | Custom server                 |

If the selected server has variables, you may override its default values through the additional parameters made available in the SDK constructor:

| Variable   | Parameter       | Default                     | Description                  |
| ---------- | --------------- | --------------------------- | ---------------------------- |
| `base_url` | `base_url: str` | `"https://pv.inteless.com"` | Base URL for the Sunsynk API |

#### Example

```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    server_idx=2,
    base_url="https://pv.inteless.com",
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.authentication.post_oauth_token(username="Florencio.Stiedemann", password="yES5j6h4HZfL6Pn", grant_type="password", client_id="csp-web")

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    server_url="https://https://pv.inteless.com",
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.authentication.post_oauth_token(username="Florencio.Stiedemann", password="yES5j6h4HZfL6Pn", grant_type="password", client_id="csp-web")

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from sunsynk_api_client import SunSynk
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SunSynk(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from sunsynk_api_client import SunSynk
from sunsynk_api_client.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SunSynk(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SunSynk` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import os
from sunsynk_api_client import SunSynk
def main():

    with SunSynk(
        bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
    ) as sun_synk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SunSynk(
        bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
    ) as sun_synk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from sunsynk_api_client import SunSynk
import logging

logging.basicConfig(level=logging.DEBUG)
s = SunSynk(debug_logger=logging.getLogger("sunsynk_api_client"))
```

You can also enable a default debug logger by setting an environment variable `SUNSYNK_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=sunsynk-api-client&utm_campaign=python)
