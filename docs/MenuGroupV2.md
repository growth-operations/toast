# MenuGroupV2

Information about a menu group configured for this restaurant, including an array of menu items contained in the group. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this menu group, for example, \&quot;Appetizers\&quot; or \&quot;Sandwiches\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this menu group, assigned by the Toast POS system.  | [optional] 
**multi_location_id** | **str** | An identifier that is used to identify and consolidate menu entities that are versions of each other. | [optional] 
**master_id** | **int** | This value is deprecated. Instead of masterId, use multiLocationId. | [optional] 
**description** | **str** | An optional short description of this menu group.  | [optional] 
**pos_name** | **str** | The button label name that appears for this menu entity in the Toast POS app. | [optional] 
**pos_button_color_light** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in light mode. | [optional] 
**pos_button_color_dark** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in dark mode. | [optional] 
**image** | **str** | The URL to an image that has been uploaded for this menu entity. | [optional] 
**visibility** | **List[str]** | An array of strings that indicate where this menu entity is visible. | [optional] 
**item_tags** | [**List[ItemTagV2]**](ItemTagV2.md) | An array of &#x60;ItemTag&#x60; objects that are assigned to this menu group. Item tags are used to assign identifying characteristics, for example, vegetarian, gluten-free, or alcohol.  | [optional] 
**menu_groups** | [**List[MenuGroupV2]**](MenuGroupV2.md) | An array of the &#x60;MenuGroup&#x60; objects that are children of this menu group. The array is empty if the menu group has no child menu groups.  | [optional] 
**menu_items** | [**List[MenuItemV2]**](MenuItemV2.md) | An array of the &#x60;MenuItem&#x60; objects contained in this menu group.  | [optional] 

## Example

```python
from toastapi.models.menu_group_v2 import MenuGroupV2

# TODO update the JSON string below
json = "{}"
# create an instance of MenuGroupV2 from a JSON string
menu_group_v2_instance = MenuGroupV2.from_json(json)
# print the JSON string representation of the object
print(MenuGroupV2.to_json())

# convert the object into a dict
menu_group_v2_dict = menu_group_v2_instance.to_dict()
# create an instance of MenuGroupV2 from a dict
menu_group_v2_from_dict = MenuGroupV2.from_dict(menu_group_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


