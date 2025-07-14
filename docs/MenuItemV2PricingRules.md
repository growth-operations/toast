# MenuItemV2PricingRules

A `PricingRules` object with information about how to calculate the price for this menu item. You use a menu item's `pricingRules` value, in conjunction with its `pricingStrategy` value, to calculate a price for a menu item that uses a size-specific or time-specific price.  The `pricingRules` object takes different forms depending on the pricing strategy configured for the menu item. Use the `pricingStrategy` value to determine which pricing strategy has been used so that you can properly interpret the data in the `pricingRules` object. For the BASE_PRICE, and MENU_SPECIFIC_PRICE pricing strategies, the `pricingRules` object is null because you can retrieve the price from the `price` value without additional calculation. For the OPEN_PRICE pricing strategy, the `pricingRules` object is also null (the price of an open menu item is specified when it is ordered). For the TIME_SPECIFIC_PRICE and SIZE_PRICE pricing strategies, the `PricingRules` object contains additional values that you use to calculate the menu item's price. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_specific_pricing_rules** | [**List[TimeSpecificPriceV2]**](TimeSpecificPriceV2.md) | An array of &#x60;TimeSpecificPrice&#x60; objects that define the time-specific prices for a menu item or modifier option &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/platformguide/adminPricingModifierOptions.html#adminUnderstandingAModifierOptionsItemReference\&quot;&gt;item reference&lt;/a&gt; that uses the Time Specific Price pricing strategy. If the menu item or modifier option item reference does not use time-specific prices, this array is empty.  | [optional] 
**size_specific_pricing_guid** | **str** | The GUID of a Size modifier group that defines sizes and prices for a menu item or a modifier option item reference that uses the Size Price pricing strategy.  If the menu item or modifier option item reference does not use the Size Price pricing strategy, then &#x60;sizeSpecificPricingGuid&#x60; is null.  The Toast POS system automatically creates a Size modifier group when you choose the Size Price pricing strategy for a menu item or modifier option item reference and stores the sizes and prices you specify in it. You use the &#x60;sizeSpecificPricingGuid&#x60; value to locate the correct Size modifier group to use when pricing a menu item or modifier option item reference that uses size pricing.  When the &#x60;PricingRules&#x60; object appears in the context of a modifier group, the &#x60;sizeSpecificPricingGuid&#x60; value it contains is also used to find matching sizes between menu items and any modifier options that use the Size Price or Size/Sequence Pricing pricing strategies (for example, toppings on a small pizza cost $1 while toppings on a large pizza cost $2). In this scenario, the Toast POS system locates the modifier option size that matches the menu item size and uses the price defined for that size of the modifier option. The sizes for the menu item are defined in the Size modifier group specified by the &#x60;sizeSpecificPricingGuid&#x60; value. The sizes for the modifier options are defined in objects contained in the &#x60;sizeSequencePricingRules&#x60; array that is contained in the modifier group&#39;s &#x60;PricingRules&#x60; object. Sizes are considered matching when their names are identical.  For detailed information on the **Size Price** and **Size/Sequence Price** pricing strategies, see the Pricing Strategies section in the Toast Platform Guide.  | [optional] 
**size_sequence_pricing_rules** | [**List[SizeSequencePricingRuleV2]**](SizeSequencePricingRuleV2.md) | An array of &#x60;SizeSequencePricingRule&#x60; objects that define the prices for the modifier options in a modifier group that uses the Size Price, Sequence Price, or Size/Sequence Pricing pricing strategy. If the modifier group does not use one of these pricing strategies, this array is empty.  | [optional] 

## Example

```python
from toastapi.models.menu_item_v2_pricing_rules import MenuItemV2PricingRules

# TODO update the JSON string below
json = "{}"
# create an instance of MenuItemV2PricingRules from a JSON string
menu_item_v2_pricing_rules_instance = MenuItemV2PricingRules.from_json(json)
# print the JSON string representation of the object
print(MenuItemV2PricingRules.to_json())

# convert the object into a dict
menu_item_v2_pricing_rules_dict = menu_item_v2_pricing_rules_instance.to_dict()
# create an instance of MenuItemV2PricingRules from a dict
menu_item_v2_pricing_rules_from_dict = MenuItemV2PricingRules.from_dict(menu_item_v2_pricing_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


