# SizeSequencePricingRuleV2

Defines the pricing rules for modifier options that belong to a modifier group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_name** | **str** | A string that represents the size of a modifier option. | [optional] 
**size_guid** | **str** | The GUID of the modifier option where a menu item size has been defined. | [optional] 
**sequence_prices** | [**List[SequencePriceV2]**](SequencePriceV2.md) | An array of SequencePrice objects. | [optional] 

## Example

```python
from toastapi.models.size_sequence_pricing_rule_v2 import SizeSequencePricingRuleV2

# TODO update the JSON string below
json = "{}"
# create an instance of SizeSequencePricingRuleV2 from a JSON string
size_sequence_pricing_rule_v2_instance = SizeSequencePricingRuleV2.from_json(json)
# print the JSON string representation of the object
print(SizeSequencePricingRuleV2.to_json())

# convert the object into a dict
size_sequence_pricing_rule_v2_dict = size_sequence_pricing_rule_v2_instance.to_dict()
# create an instance of SizeSequencePricingRuleV2 from a dict
size_sequence_pricing_rule_v2_from_dict = SizeSequencePricingRuleV2.from_dict(size_sequence_pricing_rule_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


