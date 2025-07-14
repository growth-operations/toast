# AuthenticationRequest

Authentication credentials for your Toast API integration client software. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The identifier string for your Toast API client. You receive the identifier string from the Toast integrations team.  | 
**client_secret** | **str** | The secret string that corresponds to your Toast API client. You receive the secret string from the Toast integrations team.  | 
**user_access_type** | **str** | Always include the &#x60;userAccessType&#x60; value and set it to &#x60;TOAST_MACHINE_CLIENT&#x60;.  | 

## Example

```python
from toastapi.models.authentication_request import AuthenticationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationRequest from a JSON string
authentication_request_instance = AuthenticationRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticationRequest.to_json())

# convert the object into a dict
authentication_request_dict = authentication_request_instance.to_dict()
# create an instance of AuthenticationRequest from a dict
authentication_request_from_dict = AuthenticationRequest.from_dict(authentication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


