# ModifierGroup

Information about a modifier group configured for this restaurant, including an array of modifier options contained in the group. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this modifier group, for example, \&quot;Pizza Toppings\&quot; or \&quot;Salad Dressings\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this modifier group, assigned by the Toast POS system.  | [optional] 
**reference_id** | **int** | An integer identifier that is used to refer to this modifier group by items and portions that use it.  | [optional] 
**multi_location_id** | **str** | An identifier that is used to identify and consolidate menu entities that are versions of each other.  &#x60;multiLocationId&#x60; replaces &#x60;masterId&#x60;. &#x60;multiLocationId&#x60; and &#x60;masterId&#x60; always have the same value.  Menu entities can be versioned. Those versions can be assigned to specific restaurant locations, or groups of locations, in a management group. For example, you could have two versions of a burger, one for a Boston location and another for a New York City location. Versioned menu entities share the majority of, but not all of, their data. For example, the Boston version is called the Minuteman Burger and has pickles, while the New York City version is called the Empire Burger and does not.  You use the &#x60;multiLocationId&#x60; to identify menu entities that are versions of each other. To continue the example above, the Minuteman Burger in the JSON returned for the Boston location has the same &#x60;multilocationId&#x60; as the Empire Burger in the JSON returned for the New York City location. These matching &#x60;multlocationId&#x60; values indicate that the two items are related versions of the same item. In Toast reports, this allows a restaurant to track sales of the burger across both locations.  | [optional] 
**master_id** | **int** | This value is deprecated. Instead of &#x60;masterId&#x60;, use &#x60;multiLocationId&#x60;.  An identifier that is used to identify and consolidate menu entities that are versions of each other.  | [optional] 
**pos_name** | **str** | The button label name that appears for this menu entity in the Toast POS app. &#x60;posName&#x60; contains an empty string if a &#x60;posName&#x60; has not been defined for the menu entity and the &#x60;name&#x60; value is used for the button label instead.  | [optional] 
**pos_button_color_light** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in light mode.       When an employee configures a POS button&#39;s color, they select a color pairing that consists of two colors, one for light mode and one for dark mode. &#x60;posButtonColorLight&#x60; contains the HEX code for the light mode color.  | [optional] 
**pos_button_color_dark** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in dark mode.       When an employee configures a POS button&#39;s color, they select a color pairing that consists of two colors, one for light mode and one for dark mode. &#x60;posButtonColorDark&#x60; contains the HEX code for the dark mode color.  | [optional] 
**visibility** | [**Visibility**](Visibility.md) |  | [optional] 
**pricing_strategy** | **str** | A string that represents the pricing strategy used for this modifier group.  If there is no additional charge for the modifier options in this group, or if the modifier options in the group are priced individually, then the &#x60;pricingStrategy&#x60; value is NONE.  If the modifier group is priced at the group level and is using the:   * Fixed Price pricing strategy, then the &#x60;pricingStrategy&#x60; value is NONE.   * Sequence Price pricing strategy, then the &#x60;pricingStrategy&#x60; value is SEQUENCE_PRICE.   * Size Price pricing strategy, then the &#x60;pricingStrategy&#x60; value is SIZE_PRICE.   * Size/Sequence Price pricing strategy, then the &#x60;pricingStrategy&#x60; value is SIZE_SEQUENCE_PRICE.     If the &#x60;pricingStrategy&#x60; value is NONE,  then the prices for the modifier options in this group are resolved down to the modifier option level and you can retrieve them from the &#x60;price&#x60; value of the individual &#x60;ModifierOption&#x60; objects.  If the &#x60;pricingStrategy&#x60; value is SIZE_PRICE, SEQUENCE_PRICE, or SIZE_SEQUENCE_PRICE, then you must use the rules provided in _this modifier group&#39;s_ &#x60;pricingRules&#x60; value to calculate the prices for the modifier options in the group.  | [optional] 
**pricing_rules** | [**PricingRules**](.md) |  | [optional] 
**default_options_charge_price** | **str** | Indicates whether the prices associated with any default modifiers in this group are added to the cost of the menu items they modify.  Values are:   * NO: The default modifier price is ignored. No change is made to the cost of the menu item.   * YES: The default modifier price is added to the menu item price. YES is the default setting for &#x60;defaultOptionsChargePrice&#x60;.  | [optional] 
**default_options_substitution_pricing** | **str** | Indicates whether substitution pricing is enabled for the modifier group.  | [optional] 
**min_selections** | **int** | The minimum number of modifier options that a customer can choose from this modifier group.  If a server is not required to select a modifier option from this modifier group, &#x60;minSelections&#x60; is set to 0.  If a server must select a modifier option from this modifier group, &#x60;minSelections&#x60; must be set to 1 or higher.  | [optional] 
**max_selections** | **int** | The maximum number of modifier options that a customer can choose from this modifier group. &#x60;maxSelections&#x60; is null if a customer can choose an unlimited number of modifier options from this modifier group.  | [optional] 
**required_mode** | **str** | Specifies how the modifier group appears and behaves in the Toast POS app.  | [optional] 
**is_multi_select** | **bool** | Indicates whether you can select more than one modifier option from this modifier group.  | [optional] 
**pre_modifier_group_reference** | **int** | The &#x60;referenceId&#x60; of a &#x60;PreModifierGroup&#x60; object. This object defines the premodifiers that can be applied to the modifier options contained in this modifier group.  | [optional] 
**modifier_option_references** | **List[int]** | An array of &#x60;referenceId&#x60;s for &#x60;ModifierOption&#x60; objects. These objects define the modifier options contained in this modifier group.  | [optional] 

## Example

```python
from toastapi.models.modifier_group import ModifierGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierGroup from a JSON string
modifier_group_instance = ModifierGroup.from_json(json)
# print the JSON string representation of the object
print(ModifierGroup.to_json())

# convert the object into a dict
modifier_group_dict = modifier_group_instance.to_dict()
# create an instance of ModifierGroup from a dict
modifier_group_from_dict = ModifierGroup.from_dict(modifier_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


