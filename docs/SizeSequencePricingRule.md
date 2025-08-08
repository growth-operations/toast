# SizeSequencePricingRule

A multi-use object that defines the pricing rules for modifier options that belong to a modifier group that uses the Size Price, Sequence Price, or Size/Sequence Price pricing strategy. The contents of this object depend on the pricing strategy that is in effect. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_name** | **str** | A string that represents the size of a modifier option in this modifier group, for example, Small, Medium, or Large.  With Size Price and the Size/Sequence Price pricing strategies, the price of a modifier option changes based on the size of the menu item it is applied to. The &#x60;sizeName&#x60; value is null if the modifier group uses the Sequence Price pricing strategy because this strategy does not use sizes.  | [optional] 
**size_guid** | **str** | The GUID of the modifier option where a menu item size has been defined that matches the &#x60;sizeName&#x60; value. The &#x60;sizeGuid&#x60; value is null if the modifier group uses the Sequence Price pricing strategy because this strategy does not use sizes.  | [optional] 
**sequence_prices** | [**List[SequencePrice]**](SequencePrice.md) | An array of &#x60;SequencePrice&#x60; objects that define the size, sequence, or size/sequence prices for the modifier options in this modifier group.  | [optional] 

## Example

```python
from toastapi.models.size_sequence_pricing_rule import SizeSequencePricingRule

# TODO update the JSON string below
json = "{}"
# create an instance of SizeSequencePricingRule from a JSON string
size_sequence_pricing_rule_instance = SizeSequencePricingRule.from_json(json)
# print the JSON string representation of the object
print(SizeSequencePricingRule.to_json())

# convert the object into a dict
size_sequence_pricing_rule_dict = size_sequence_pricing_rule_instance.to_dict()
# create an instance of SizeSequencePricingRule from a dict
size_sequence_pricing_rule_from_dict = SizeSequencePricingRule.from_dict(size_sequence_pricing_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


