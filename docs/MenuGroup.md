# MenuGroup

Information about a menu group configured for this restaurant, including an array of menu items contained in the group. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this menu group, for example, \&quot;Appetizers\&quot; or \&quot;Sandwiches\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this menu group, assigned by the Toast POS system.  | [optional] 
**multi_location_id** | **str** | An identifier that is used to identify and consolidate menu entities that are versions of each other.  &#x60;multiLocationId&#x60; replaces &#x60;masterId&#x60;. &#x60;multiLocationId&#x60; and &#x60;masterId&#x60; always have the same value.  Menu entities can be versioned. Those versions can be assigned to specific restaurant locations, or groups of locations, in a management group. For example, you could have two versions of a burger, one for a Boston location and another for a New York City location. Versioned menu entities share the majority of, but not all of, their data. For example, the Boston version is called the Minuteman Burger and has pickles, while the New York City version is called the Empire Burger and does not.  You use the &#x60;multiLocationId&#x60; to identify menu entities that are versions of each other. To continue the example above, the Minuteman Burger in the JSON returned for the Boston location has the same &#x60;multilocationId&#x60; as the Empire Burger in the JSON returned for the New York City location. These matching &#x60;multlocationId&#x60; values indicate that the two items are related versions of the same item. In Toast reports, this allows a restaurant to track sales of the burger across both locations.  | [optional] 
**master_id** | **int** | This value is deprecated. Instead of &#x60;masterId&#x60;, use &#x60;multiLocationId&#x60;.  An identifier that is used to identify and consolidate menu entities that are versions of each other.  | [optional] 
**description** | **str** | An optional short description of this menu group.  | [optional] 
**pos_name** | **str** | The button label name that appears for this menu entity in the Toast POS app. &#x60;posName&#x60; contains an empty string if a &#x60;posName&#x60; has not been defined for the menu entity and the &#x60;name&#x60; value is used for the button label instead.  | [optional] 
**pos_button_color_light** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in light mode.       When an employee configures a POS button&#39;s color, they select a color pairing that consists of two colors, one for light mode and one for dark mode. &#x60;posButtonColorLight&#x60; contains the HEX code for the light mode color.  | [optional] 
**pos_button_color_dark** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in dark mode.       When an employee configures a POS button&#39;s color, they select a color pairing that consists of two colors, one for light mode and one for dark mode. &#x60;posButtonColorDark&#x60; contains the HEX code for the dark mode color.  | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**visibility** | **List[str]** | An array of strings that indicate where this menu entity is visible:  * POS: The menu entity is visible in the Toast POS app.   * KIOSK: The menu entity is visible on a Toast kiosk.   * TOAST_ONLINE_ORDERING: The menu entity is visible in the Toast online   ordering site for this restaurant.   * ORDERING_PARTNERS: The restaurants wants this menu entity to be visible   on online ordering sites that integrate with the Toast POS system using the orders API.   * GRUBHUB: Deprecated. The menu entity is included during a menu sync to   Grubhub and will be visible on the Grubhub online ordering service after a   menu sync has completed. _Note:_ Conceptually, the _Grubhub_ configuration   option that was associated with the &#x60;GRUBHUB&#x60; string in this array has   been replaced by the more general _Online orders: Ordering partners_   configuration option and restaurants that used the _Grubhub_ option have   been automatically migrated to the new _Online orders: Ordering partners_   option. This means that any menu entity that had the _Grubhub_ option set   to _Yes_ will now have the _Online orders: Ordering partners_ option   enabled and the &#x60;ORDERING_PARTNERS&#x60; enum will be present in the   &#x60;visibility&#x60; array for it. To support backwards compatibility, the   &#x60;visibility&#x60; array for these entities will also continue to contain the   &#x60;GRUBHUB&#x60; enum for a short period of time. See &lt;a   href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiDeprecatedApiFunctions.html#apiMenuEntityVisibilityEnhancements\&quot;&gt;Menu   Visibility Enhancements (Rolled Out)&lt;/a&gt; for more information.  The &#x60;visibility&#x60; array is empty if the menu entity is not configured to be visible for any of the use cases listed above.  | [optional] 
**item_tags** | [**List[ItemTag]**](ItemTag.md) | An array of &#x60;ItemTag&#x60; objects that are assigned to this menu group. Item tags are used to assign identifying characteristics, for example, vegetarian, gluten-free, or alcohol.  | [optional] 
**menu_groups** | [**List[MenuGroup]**](MenuGroup.md) | An array of the &#x60;MenuGroup&#x60; objects that are children of this menu group. The array is empty if the menu group has no child menu groups.  | [optional] 
**menu_items** | [**List[MenuItem]**](MenuItem.md) | An array of the &#x60;MenuItem&#x60; objects contained in this menu group.  | [optional] 

## Example

```python
from toastapi.models.menu_group import MenuGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MenuGroup from a JSON string
menu_group_instance = MenuGroup.from_json(json)
# print the JSON string representation of the object
print(MenuGroup.to_json())

# convert the object into a dict
menu_group_dict = menu_group_instance.to_dict()
# create an instance of MenuGroup from a dict
menu_group_from_dict = MenuGroup.from_dict(menu_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


