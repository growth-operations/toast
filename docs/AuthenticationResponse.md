# AuthenticationResponse

A wrapper object for the response to a successful Toast API authentication request. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**AuthenticationToken**](AuthenticationToken.md) |  | [optional] 
**status** | **str** | The value &#x60;SUCCESS&#x60; indicates that your authentication request was successful. | [optional] 

## Example

```python
from toastapi.models.authentication_response import AuthenticationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationResponse from a JSON string
authentication_response_instance = AuthenticationResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationResponse.to_json())

# convert the object into a dict
authentication_response_dict = authentication_response_instance.to_dict()
# create an instance of AuthenticationResponse from a dict
authentication_response_from_dict = AuthenticationResponse.from_dict(authentication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


