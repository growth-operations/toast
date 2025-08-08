# ModifierOptionTaxInfo

Information about the tax rates and tax behavior of this modifier option. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_rate_guids** | **List[str]** | An array of GUIDs for the tax rates that apply to this modifier option.  | [optional] 

## Example

```python
from toastapi.models.modifier_option_tax_info import ModifierOptionTaxInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierOptionTaxInfo from a JSON string
modifier_option_tax_info_instance = ModifierOptionTaxInfo.from_json(json)
# print the JSON string representation of the object
print(ModifierOptionTaxInfo.to_json())

# convert the object into a dict
modifier_option_tax_info_dict = modifier_option_tax_info_instance.to_dict()
# create an instance of ModifierOptionTaxInfo from a dict
modifier_option_tax_info_from_dict = ModifierOptionTaxInfo.from_dict(modifier_option_tax_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


