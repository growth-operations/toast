# ErrorMessage

An object that contains information about one or more errors that the Toast platform encountered when processing your API request. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The HTTP status code of the response.  | [optional] 
**code** | **int** | A numeric identifier for the error condition.  | [optional] 
**message** | **str** | A description of the error condition.  | [optional] 
**message_key** | **str** | Reserved for future use.  | [optional] 
**field_name** | **str** | Reserved for future use.  | [optional] 
**link** | **str** | The URL of a resource that provides more information about the error condition.  | [optional] 
**request_id** | **str** | The unique identifier of the HTTP request that your client sent to the Toast API.  | [optional] 
**developer_message** | **str** | Additional detail about the error condition, if it is available.  | [optional] 
**errors** | [**List[ErrorMessage]**](ErrorMessage.md) | A JSON array of &#x60;ErrorMessage&#x60; objects.  | [optional] 
**can_retry** | **str** | Reserved for future use.  | [optional] 

## Example

```python
from toastapi.models.error_message import ErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMessage from a JSON string
error_message_instance = ErrorMessage.from_json(json)
# print the JSON string representation of the object
print(ErrorMessage.to_json())

# convert the object into a dict
error_message_dict = error_message_instance.to_dict()
# create an instance of ErrorMessage from a dict
error_message_from_dict = ErrorMessage.from_dict(error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


