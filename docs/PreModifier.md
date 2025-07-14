# PreModifier

Information about a pre-modifier option configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this pre-modifier option.  | [optional] 
**guid** | **str** | A unique identifier for this pre-modifier option, assigned by the Toast POS system.  | [optional] 
**fixed_price** | **float** | The fixed price of this pre-modifier option.  | [optional] 
**display_mode** | **str** | The display mode for this pre-modifier option.  | [optional] 

## Example

```python
from toastapi.models.pre_modifier import PreModifier

# TODO update the JSON string below
json = "{}"
# create an instance of PreModifier from a JSON string
pre_modifier_instance = PreModifier.from_json(json)
# print the JSON string representation of the object
print(PreModifier.to_json())

# convert the object into a dict
pre_modifier_dict = pre_modifier_instance.to_dict()
# create an instance of PreModifier from a dict
pre_modifier_from_dict = PreModifier.from_dict(pre_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


