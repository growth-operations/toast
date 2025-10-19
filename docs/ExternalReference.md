# ExternalReference

A wrapper object with fields that allow reference to a Toast platform entity by Toast GUID or a partner's identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 

## Example

```python
from toastapi.models.external_reference import ExternalReference

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalReference from a JSON string
external_reference_instance = ExternalReference.from_json(json)
# print the JSON string representation of the object
print(ExternalReference.to_json())

# convert the object into a dict
external_reference_dict = external_reference_instance.to_dict()
# create an instance of ExternalReference from a dict
external_reference_from_dict = ExternalReference.from_dict(external_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


