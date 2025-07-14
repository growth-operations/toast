# PreModifierGroupV2

Information about a pre-modifier group configured for this restaurant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this pre-modifier group. | [optional] 
**guid** | **str** | A unique identifier for this pre-modifier group. | [optional] 
**pre_modifiers** | [**List[PreModifierV2]**](PreModifierV2.md) | An array of PreModifier objects. | [optional] 

## Example

```python
from toastapi.models.pre_modifier_group_v2 import PreModifierGroupV2

# TODO update the JSON string below
json = "{}"
# create an instance of PreModifierGroupV2 from a JSON string
pre_modifier_group_v2_instance = PreModifierGroupV2.from_json(json)
# print the JSON string representation of the object
print(PreModifierGroupV2.to_json())

# convert the object into a dict
pre_modifier_group_v2_dict = pre_modifier_group_v2_instance.to_dict()
# create an instance of PreModifierGroupV2 from a dict
pre_modifier_group_v2_from_dict = PreModifierGroupV2.from_dict(pre_modifier_group_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


