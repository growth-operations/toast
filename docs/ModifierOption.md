# ModifierOption

Information about a modifier option configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this modifier option.  | [optional] 
**guid** | **str** | A unique identifier for this modifier option, assigned by the Toast POS system.  | [optional] 
**reference_id** | **int** | A reference identifier for this modifier option.  | [optional] 
**price** | **float** | The price of this modifier option.  | [optional] 

## Example

```python
from toastapi.models.modifier_option import ModifierOption

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierOption from a JSON string
modifier_option_instance = ModifierOption.from_json(json)
# print the JSON string representation of the object
print(ModifierOption.to_json())

# convert the object into a dict
modifier_option_dict = modifier_option_instance.to_dict()
# create an instance of ModifierOption from a dict
modifier_option_from_dict = ModifierOption.from_dict(modifier_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


