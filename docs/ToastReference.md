# ToastReference

A wrapper object with fields that allow reference to a Toast entity by Toast GUID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 

## Example

```python
from toastapi.models.toast_reference import ToastReference

# TODO update the JSON string below
json = "{}"
# create an instance of ToastReference from a JSON string
toast_reference_instance = ToastReference.from_json(json)
# print the JSON string representation of the object
print(ToastReference.to_json())

# convert the object into a dict
toast_reference_dict = toast_reference_instance.to_dict()
# create an instance of ToastReference from a dict
toast_reference_from_dict = ToastReference.from_dict(toast_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


