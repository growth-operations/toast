# VoidReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**name** | **str** | The name of this void reason. | [optional] 

## Example

```python
from toastapi.models.void_reason import VoidReason

# TODO update the JSON string below
json = "{}"
# create an instance of VoidReason from a JSON string
void_reason_instance = VoidReason.from_json(json)
# print the JSON string representation of the object
print(VoidReason.to_json())

# convert the object into a dict
void_reason_dict = void_reason_instance.to_dict()
# create an instance of VoidReason from a dict
void_reason_from_dict = VoidReason.from_dict(void_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


