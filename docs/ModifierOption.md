# ModifierOption

Information about a modifier option configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **int** | An integer identifier that is used to refer to this modifier option by modifier option groups that contain it.  | [optional] 
**name** | **str** | A descriptive name for this modifier option, for example, \&quot;Cheese\&quot; or \&quot;Pepperoni\&quot;.  | [optional] 
**kitchen_name** | **str** | The name of the modifier option as it appears on kitchen tickets. The &#x60;kitchenName&#x60; can include both numbers and letters. This value contains an empty string if a kitchen name has not been configured for the modifier option.  | [optional] 
**guid** | **str** | A unique identifier for this modifier option&#39;s item reference, assigned by the Toast POS system.  | [optional] 
**multi_location_id** | **str** | An identifier that is used to identify and consolidate menu entities that are versions of each other.  &#x60;multiLocationId&#x60; replaces &#x60;masterId&#x60;. &#x60;multiLocationId&#x60; and &#x60;masterId&#x60; always have the same value.  Menu entities can be versioned. Those versions can be assigned to specific restaurant locations, or groups of locations, in a management group. For example, you could have two versions of a burger, one for a Boston location and another for a New York City location. Versioned menu entities share the majority of, but not all of, their data. For example, the Boston version is called the Minuteman Burger and has pickles, while the New York City version is called the Empire Burger and does not.  You use the &#x60;multiLocationId&#x60; to identify menu entities that are versions of each other. To continue the example above, the Minuteman Burger in the JSON returned for the Boston location has the same &#x60;multilocationId&#x60; as the Empire Burger in the JSON returned for the New York City location. These matching &#x60;multlocationId&#x60; values indicate that the two items are related versions of the same item. In Toast reports, this allows a restaurant to track sales of the burger across both locations.  | [optional] 
**master_id** | **int** | This value is deprecated. Instead of &#x60;masterId&#x60;, use &#x60;multiLocationId&#x60;.  An identifier that is used to identify and consolidate menu entities that are versions of each other.  | [optional] 
**description** | **str** | An optional short description of this modifier option.  | [optional] 
**pos_name** | **str** | The button label name that appears for this menu entity in the Toast POS app. &#x60;posName&#x60; contains an empty string if a &#x60;posName&#x60; has not been defined for the menu entity and the &#x60;name&#x60; value is used for the button label instead.  | [optional] 
**pos_button_color_light** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in light mode.       When an employee configures a POS button&#39;s color, they select a color pairing that consists of two colors, one for light mode and one for dark mode. &#x60;posButtonColorLight&#x60; contains the HEX code for the light mode color.  | [optional] 
**pos_button_color_dark** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in dark mode.       When an employee configures a POS button&#39;s color, they select a color pairing that consists of two colors, one for light mode and one for dark mode. &#x60;posButtonColorDark&#x60; contains the HEX code for the dark mode color.  | [optional] 
**prep_stations** | **List[str]** | An array of GUIDs for the prep stations that have been assigned to this modifier option.  | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**visibility** | **List[str]** | An array of strings that indicate where this menu entity is visible:  * POS: The menu entity is visible in the Toast POS app.   * KIOSK: The menu entity is visible on a Toast kiosk.   * TOAST_ONLINE_ORDERING: The menu entity is visible in the Toast online   ordering site for this restaurant.   * ORDERING_PARTNERS: The restaurants wants this menu entity to be visible   on online ordering sites that integrate with the Toast POS system using the orders API.   * GRUBHUB: Deprecated. The menu entity is included during a menu sync to   Grubhub and will be visible on the Grubhub online ordering service after a   menu sync has completed. _Note:_ Conceptually, the _Grubhub_ configuration   option that was associated with the &#x60;GRUBHUB&#x60; string in this array has   been replaced by the more general _Online orders: Ordering partners_   configuration option and restaurants that used the _Grubhub_ option have   been automatically migrated to the new _Online orders: Ordering partners_   option. This means that any menu entity that had the _Grubhub_ option set   to _Yes_ will now have the _Online orders: Ordering partners_ option   enabled and the &#x60;ORDERING_PARTNERS&#x60; enum will be present in the   &#x60;visibility&#x60; array for it. To support backwards compatibility, the   &#x60;visibility&#x60; array for these entities will also continue to contain the   &#x60;GRUBHUB&#x60; enum for a short period of time. See &lt;a   href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiDeprecatedApiFunctions.html#apiMenuEntityVisibilityEnhancements\&quot;&gt;Menu   Visibility Enhancements (Rolled Out)&lt;/a&gt; for more information.  The &#x60;visibility&#x60; array is empty if the menu entity is not configured to be visible for any of the use cases listed above.  | [optional] 
**price** | **float** | The price of this modifier option.  In Toast Web, a modifier option may:   * Inherit its price from a parent modifier group.   * Use the price specified for its modifier option item reference.   * Specify a price that overrides the price defined for its item reference.  The &#x60;price&#x60; value is populated differently depending on which of these pricing scenarios is used for the modifier option.  | [optional] 
**pricing_strategy** | **str** | A string that indicates how this modifier option has been priced. If &#x60;pricingStrategy&#x60; is:   * GROUP_PRICE, then the modifier option inherits its price from a parent modifier group.   * Any value other than GROUP_PRICE, then the modifier option is using either the price specified for its item reference or an override price.  | [optional] 
**pricing_rules** | [**PricingRules**](.md) |  | [optional] 
**sales_category** | [**SalesCategory**](SalesCategory.md) |  | [optional] 
**tax_info** | **List[str]** | The &#x60;taxInfo&#x60; value on the &#x60;ModifierOption&#x60; object has been deprecated. Your integration should switch to using the &#x60;modifierOptionTaxInfo&#x60; value instead.  | [optional] 
**modifier_option_tax_info** | [**ModifierOptionTaxInfo**](ModifierOptionTaxInfo.md) |  | [optional] 
**item_tags** | [**List[ItemTag]**](ItemTag.md) | An array of &#x60;ItemTag&#x60; objects that are assigned to this modifier option. Item tags are used to assign identifying characteristics to a modifier option, for example, vegetarian, gluten-free, alcohol.  | [optional] 
**plu** | **str** | The price lookup (PLU) code for this modifier option. The PLU code can contain both numbers and letters. This value contains an empty string if a PLU code has not been defined.  | [optional] 
**sku** | **str** | The stock keeping unit (SKU) identifier for this modifier option. The SKU identifier can contain both numbers and letters. This value contains an empty string if a SKU has not been defined.  | [optional] 
**calories** | **int** | The number of calories in this modifier option. The calories value can be any positive or negative integer, or zero. This value is null if a calories amount has not been configured for the modifier option.  | [optional] 
**content_advisories** | [**ContentAdvisories**](ContentAdvisories.md) |  | [optional] 
**unit_of_measure** | **str** | The unit of measure used to determine the price of the modifier option. For example, $10.00 per gram.  | [optional] 
**is_default** | **bool** | Indicates whether this modifier option is included on the menu item by default.  | [optional] 
**allows_duplicates** | **bool** | Indicates whether the modifier option may be added to a menu item multiple times.  | [optional] 
**portions** | [**List[Portion]**](Portion.md) | An array of &#x60;Portion&#x60; objects that define the portions that this modifier option can be added to.  | [optional] 
**prep_time** | **int** | The amount of time, in seconds, that it takes to prepare this modifier option. This value is null if a prep time has not been specified for the modifier option.  | [optional] 
**modifier_group_references** | **List[int]** | An array of &#x60;referenceId&#x60;s for &#x60;ModifierGroup&#x60; objects. These objects define nested modifier groups contained in this modifier option.  | [optional] 
**length** | **float** | The length of the item or modifier. Use the &#x60;dimensionUnitOfMeasure&#x60; value to determine the unit of measurement.  The &#x60;length&#x60; value is &#x60;null&#x60; if no length is specified for the item or modifier.  You can use the &#x60;length&#x60;, &#x60;height&#x60;, and &#x60;width&#x60; values to determine the overall size of the item or modifier. This information is useful, for example, when determining shipping costs or choosing the size of delivery vehicle to use.  | [optional] 
**height** | **float** | The height of the item or modifier. Use the &#x60;dimensionUnitOfMeasure&#x60; value to determine the unit of measurement.  The &#x60;height&#x60; value is &#x60;null&#x60; if no height is specified for the item or modifier.  You can use the &#x60;length&#x60;, &#x60;height&#x60;, and &#x60;width&#x60; values to determine the overall size of the item or modifier. This information is useful, for example, when determining shipping costs or choosing the size of delivery vehicle to use.  | [optional] 
**width** | **float** | The width of the item or modifier. Use the &#x60;dimensionUnitOfMeasure&#x60; value to determine the unit of measurement.  The &#x60;width&#x60; value is &#x60;null&#x60; if no width is specified for the item or modifier.  You can use the &#x60;length&#x60;, &#x60;height&#x60;, and &#x60;width&#x60; values to determine the overall size of the item or modifier. This information is useful, for example, when determining shipping costs or choosing the size of delivery vehicle to use.  | [optional] 
**dimension_unit_of_measure** | [**DimensionUnitOfMeasure**](DimensionUnitOfMeasure.md) |  | [optional] 
**weight** | **float** | The weight of the item or modifier. Use the &#x60;weightUnitOfMeasure&#x60; value to determine the unit of measurement.  The &#x60;weight&#x60; value is &#x60;null&#x60; if no weight is specified for the item or modifier.      You can use the &#x60;weight&#x60; value when determining shipping costs or choosing a delivery vehicle to use.  | [optional] 
**weight_unit_of_measure** | [**WeightUnitOfMeasure**](WeightUnitOfMeasure.md) |  | [optional] 
**images** | **List[str]** | An array of strings that contain URLs for images that have been uploaded for this item or modifier. The array is empty if no images have been uploaded.      _Note:_ The &#x60;images&#x60; array contains multiple URLs for multiple images for the same item or modifier. The older &#x60;image&#x60; value contains a single URL for a single image.  | [optional] 
**guest_count** | **float** | The number of guests the item or modifier is expected to serve. This value is &#x60;null&#x60; if no guest count is specified.  | [optional] 

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


