# PreModifierV2

Information about a pre-modifier configured for this restaurant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this pre-modifier. | [optional] 
**guid** | **str** | A unique identifier for this pre-modifier. | [optional] 
**fixed_price** | **float** | An optional fixed price for this pre-modifier. | [optional] 
**multiplication_factor** | **float** | An optional number that specifies how much the cost is multiplied by. | [optional] 
**display_mode** | **str** | How the pre-modifier is displayed on tickets and receipts. | [optional] 

## Example

```python
from toastapi.models.pre_modifier_v2 import PreModifierV2

# TODO update the JSON string below
json = "{}"
# create an instance of PreModifierV2 from a JSON string
pre_modifier_v2_instance = PreModifierV2.from_json(json)
# print the JSON string representation of the object
print(PreModifierV2.to_json())

# convert the object into a dict
pre_modifier_v2_dict = pre_modifier_v2_instance.to_dict()
# create an instance of PreModifierV2 from a dict
pre_modifier_v2_from_dict = PreModifierV2.from_dict(pre_modifier_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


