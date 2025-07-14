# AuthenticationToken

Information about a Toast platform API session, including an authentication token string that your Toast API client software can present when using other Toast platform APIs. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **str** | The OAuth 2 authentication scheme used for the authentication token. Toast API authentication uses the bearer authentication scheme.  | [optional] 
**scope** | **str** | The scope value in the authentication token request response is &#x60;null&#x60;. The &#x60;accessToken&#x60; JSON Web Token (JWT) contains the list of [scopes for your Toast API client](https://dev.toasttab.com/doc/devguide/apiScopes.html).  | [optional] 
**expires_in** | **int** | The number of seconds that the authentication token is valid.  | [optional] 
**access_token** | **str** | A JSON Web Token (JWT) string that contains an authentication token. You [present this string when you make requests](https://dev.toasttab.com/doc/devguide/authentication.html#using-authentication-token) to other Toast API resources. The JWT includes information about your Toast API client.  | [optional] 
**id_token** | **str** | For internal use only.  | [optional] 
**refresh_token** | **str** | For internal use only.  | [optional] 

## Example

```python
from toastapi.models.authentication_token import AuthenticationToken

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationToken from a JSON string
authentication_token_instance = AuthenticationToken.from_json(json)
# print the JSON string representation of the object
print(AuthenticationToken.to_json())

# convert the object into a dict
authentication_token_dict = authentication_token_instance.to_dict()
# create an instance of AuthenticationToken from a dict
authentication_token_from_dict = AuthenticationToken.from_dict(authentication_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


