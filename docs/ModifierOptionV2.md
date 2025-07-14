# ModifierOptionV2

Information about a modifier option configured for this restaurant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **int** | An integer identifier that is used to refer to this modifier option. | [optional] 
**name** | **str** | A descriptive name for this modifier option. | [optional] 
**guid** | **str** | A unique identifier for this modifier option. | [optional] 
**price** | **float** | The price of this modifier option. | [optional] 
**pricing_strategy** | **str** | A string that indicates how this modifier option has been priced. | [optional] 

## Example

```python
from toastapi.models.modifier_option_v2 import ModifierOptionV2

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierOptionV2 from a JSON string
modifier_option_v2_instance = ModifierOptionV2.from_json(json)
# print the JSON string representation of the object
print(ModifierOptionV2.to_json())

# convert the object into a dict
modifier_option_v2_dict = modifier_option_v2_instance.to_dict()
# create an instance of ModifierOptionV2 from a dict
modifier_option_v2_from_dict = ModifierOptionV2.from_dict(modifier_option_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


