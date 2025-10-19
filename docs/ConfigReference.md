# ConfigReference

A wrapper object containing identifier values for Toast platform entities. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**multi_location_id** | **str** | A consistent identifier for Toast platform entities.  | [optional] 
**external_id** | **str** | An external identifier that is prefixed by a naming authority.  | [optional] 

## Example

```python
from toastapi.models.config_reference import ConfigReference

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigReference from a JSON string
config_reference_instance = ConfigReference.from_json(json)
# print the JSON string representation of the object
print(ConfigReference.to_json())

# convert the object into a dict
config_reference_dict = config_reference_instance.to_dict()
# create an instance of ConfigReference from a dict
config_reference_from_dict = ConfigReference.from_dict(config_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


