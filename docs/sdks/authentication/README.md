# Authentication

## Overview

Endpoints for authentication and obtaining access tokens

### Available Operations

* [post_oauth_token](#post_oauth_token) - Authenticate user and obtain access token
* [get_bearer_token](#get_bearer_token) - Authenticate and get bearer token (new flow)
* [get_public_key](#get_public_key) - Get public key for password encryption

## post_oauth_token

OAuth2 token endpoint for user authentication. For new authentication flow, use /oauth/token/new with RSA encrypted password.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/oauth/token" method="post" path="/oauth/token" -->
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

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | User's username                                                     |
| `password`                                                          | *str*                                                               | :heavy_check_mark:                                                  | User's password                                                     |
| `grant_type`                                                        | [models.GrantType](../../models/granttype.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `client_id`                                                         | [models.ClientID](../../models/clientid.md)                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TokenResponse](../../models/tokenresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.Error               | 401                        | application/json           |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## get_bearer_token

Authenticates user with credentials and returns a bearer token. Requires RSA encryption of password with public key from /anonymous/publicKey.

### Example Usage

<!-- UsageSnippet language="python" operationID="getBearerToken" method="post" path="/oauth/token/new" -->
```python
from sunsynk_api_client import SunSynk


with SunSynk() as sun_synk:

    res = sun_synk.authentication.get_bearer_token(password="sauNiCGaWRkCfz7", username="Assunta57", area_code="sunsynk", client_id="csp-web", grant_type="password", source="sunsynk")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `password`                                                          | *str*                                                               | :heavy_check_mark:                                                  | RSA encrypted password (Base64 encoded)                             |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | User's username                                                     |
| `area_code`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `client_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `grant_type`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `source`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `nonce`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Unix timestamp for request                                          |
| `sign`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | MD5 hash of nonce + source + public key snippet                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetBearerTokenResponse](../../models/getbearertokenresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |

## get_public_key

Retrieves the RSA public key used to encrypt the password before login

### Example Usage

<!-- UsageSnippet language="python" operationID="getPublicKey" method="get" path="/anonymous/publicKey" -->
```python
import os
from sunsynk_api_client import SunSynk


with SunSynk(
    bearer_auth=os.getenv("SUNSYNK_BEARER_AUTH", ""),
) as sun_synk:

    res = sun_synk.authentication.get_public_key(nonce=736433, source="sunsynk", sign="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `nonce`                                                             | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `source`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `sign`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPublicKeyResponse](../../models/getpublickeyresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.SunSynkDefaultError | 4XX, 5XX                   | \*/\*                      |