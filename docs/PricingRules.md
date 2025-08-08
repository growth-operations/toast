# PricingRules

The PricingRules object is a multi-use object that provides pricing rules for:   * A menu item or modifier option item reference that uses the Time Specific Price or Size Price pricing strategy.   * A modifier group that uses the Size Price, Sequence Price, or Size/Sequence Price pricing strategy. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_specific_pricing_rules** | [**List[TimeSpecificPrice]**](TimeSpecificPrice.md) | An array of &#x60;TimeSpecificPrice&#x60; objects that define the time-specific prices for a menu item or modifier option item reference that uses the Time Specific Price pricing strategy. If the menu item or modifier option item reference does not use time-specific prices, this array is empty.  | [optional] 
**size_specific_pricing_guid** | **str** | The GUID of a Size modifier group that defines sizes and prices for a menu item or a modifier option item reference that uses the Size Price pricing strategy. If the menu item or modifier option item reference does not use the Size Price pricing strategy, then &#x60;sizeSpecificPricingGuid&#x60; is null.  | [optional] 
**size_sequence_pricing_rules** | [**List[SizeSequencePricingRule]**](SizeSequencePricingRule.md) | An array of &#x60;SizeSequencePricingRule&#x60; objects that define the prices for the modifier options in a modifier group that uses the Size Price, Sequence Price, or Size/Sequence Pricing pricing strategy. If the modifier group does not use one of these pricing strategies, this array is empty.  | [optional] 

## Example

```python
from toastapi.models.pricing_rules import PricingRules

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRules from a JSON string
pricing_rules_instance = PricingRules.from_json(json)
# print the JSON string representation of the object
print(PricingRules.to_json())

# convert the object into a dict
pricing_rules_dict = pricing_rules_instance.to_dict()
# create an instance of PricingRules from a dict
pricing_rules_from_dict = PricingRules.from_dict(pricing_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


