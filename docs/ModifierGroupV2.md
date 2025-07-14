# ModifierGroupV2

Information about a modifier group configured for this restaurant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this modifier group. | [optional] 
**guid** | **str** | A unique identifier for this modifier group. | [optional] 
**reference_id** | **int** | An integer identifier that is used to refer to this modifier group. | [optional] 
**pricing_strategy** | **str** | The pricing strategy used for this modifier group. | [optional] 
**modifier_option_references** | **List[int]** | An array of referenceIds for ModifierOption objects. | [optional] 

## Example

```python
from toastapi.models.modifier_group_v2 import ModifierGroupV2

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierGroupV2 from a JSON string
modifier_group_v2_instance = ModifierGroupV2.from_json(json)
# print the JSON string representation of the object
print(ModifierGroupV2.to_json())

# convert the object into a dict
modifier_group_v2_dict = modifier_group_v2_instance.to_dict()
# create an instance of ModifierGroupV2 from a dict
modifier_group_v2_from_dict = ModifierGroupV2.from_dict(modifier_group_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


