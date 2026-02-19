# GetBearerTokenRequest


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `area_code`                                     | *Optional[str]*                                 | :heavy_minus_sign:                              | N/A                                             |
| `client_id`                                     | *Optional[str]*                                 | :heavy_minus_sign:                              | N/A                                             |
| `grant_type`                                    | *Optional[str]*                                 | :heavy_minus_sign:                              | N/A                                             |
| `password`                                      | *str*                                           | :heavy_check_mark:                              | RSA encrypted password (Base64 encoded)         |
| `source`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | N/A                                             |
| `username`                                      | *str*                                           | :heavy_check_mark:                              | User's username                                 |
| `nonce`                                         | *Optional[int]*                                 | :heavy_minus_sign:                              | Unix timestamp for request                      |
| `sign`                                          | *Optional[str]*                                 | :heavy_minus_sign:                              | MD5 hash of nonce + source + public key snippet |