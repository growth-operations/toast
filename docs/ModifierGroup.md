# ModifierGroup

Information about a modifier group configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this modifier group.  | [optional] 
**guid** | **str** | A unique identifier for this modifier group, assigned by the Toast POS system.  | [optional] 
**reference_id** | **int** | A reference identifier for this modifier group.  | [optional] 
**modifier_option_references** | **List[int]** | An array of reference IDs for the modifier options in this group.  | [optional] 

## Example

```python
from toastapi.models.modifier_group import ModifierGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierGroup from a JSON string
modifier_group_instance = ModifierGroup.from_json(json)
# print the JSON string representation of the object
print(ModifierGroup.to_json())

# convert the object into a dict
modifier_group_dict = modifier_group_instance.to_dict()
# create an instance of ModifierGroup from a dict
modifier_group_from_dict = ModifierGroup.from_dict(modifier_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


