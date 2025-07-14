# PreModifierGroup

Information about a pre-modifier group configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this pre-modifier group.  | [optional] 
**guid** | **str** | A unique identifier for this pre-modifier group, assigned by the Toast POS system.  | [optional] 
**reference_id** | **int** | A reference identifier for this pre-modifier group.  | [optional] 
**pre_modifiers** | [**List[PreModifier]**](PreModifier.md) | An array of pre-modifier options in this group.  | [optional] 

## Example

```python
from toastapi.models.pre_modifier_group import PreModifierGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PreModifierGroup from a JSON string
pre_modifier_group_instance = PreModifierGroup.from_json(json)
# print the JSON string representation of the object
print(PreModifierGroup.to_json())

# convert the object into a dict
pre_modifier_group_dict = pre_modifier_group_instance.to_dict()
# create an instance of PreModifierGroup from a dict
pre_modifier_group_from_dict = PreModifierGroup.from_dict(pre_modifier_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


