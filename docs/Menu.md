# Menu

Information about a menu configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this menu, for example, \&quot;Food\&quot; or \&quot;Drinks\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this menu, assigned by the Toast POS system.  | [optional] 
**multi_location_id** | **str** | An identifier that is used to identify and consolidate menu entities that are versions of each other.  &#x60;multiLocationId&#x60; replaces &#x60;masterId&#x60;. &#x60;multiLocationId&#x60; and &#x60;masterId&#x60; always have the same value.  Menu entities can be versioned. Those versions can be assigned to specific restaurant locations, or groups of locations, in a management group. For example, you could have two versions of a burger, one for a Boston location and another for a New York City location. Versioned menu entities share the majority of, but not all of, their data. For example, the Boston version is called the Minuteman Burger and has pickles, while the New York City version is called the Empire Burger and does not.  You use the &#x60;multiLocationId&#x60; to identify menu entities that are versions of each other. To continue the example above, the Minuteman Burger in the JSON returned for the Boston location has the same &#x60;multilocationId&#x60; as the Empire Burger in the JSON returned for the New York City location. These matching &#x60;multlocationId&#x60; values indicate that the two items are related versions of the same item. In Toast reports, this allows a restaurant to track sales of the burger across both locations.  | [optional] 
**master_id** | **int** | This value is deprecated. Instead of &#x60;masterId&#x60;, use &#x60;multiLocationId&#x60;.  An identifier that is used to identify and consolidate menu entities that are versions of each other.  | [optional] 
**description** | **str** | An optional short description for this menu.  | [optional] 
**pos_name** | **str** | The button label name that appears for this menu entity in the Toast POS app. &#x60;posName&#x60; contains an empty string if a &#x60;posName&#x60; has not been defined for the menu entity and the &#x60;name&#x60; value is used for the button label instead.  | [optional] 
**pos_button_color_light** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in light mode.       When an employee configures a POS button&#39;s color, they select a color pairing that consists of two colors, one for light mode and one for dark mode. &#x60;posButtonColorLight&#x60; contains the HEX code for the light mode color.  | [optional] 
**pos_button_color_dark** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in dark mode.       When an employee configures a POS button&#39;s color, they select a color pairing that consists of two colors, one for light mode and one for dark mode. &#x60;posButtonColorDark&#x60; contains the HEX code for the dark mode color.  | [optional] 
**high_res_image** | **str** | The URL to a high resolution image that has been uploaded for this menu. The image file must be in JPG, PNG, or SVG format. The &#x60;highResImage&#x60; value is only available if the Toast Kiosk module has been enabled for this restaurant. This value is null if no high resolution image has been specified.  | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**visibility** | [**Visibility**](Visibility.md) |  | [optional] 
**availability** | [**Availability**](Availability.md) |  | [optional] 
**menu_groups** | [**List[MenuGroup]**](MenuGroup.md) | An array of the &#x60;MenuGroup&#x60; objects contained in this menu.  | [optional] 

## Example

```python
from toastapi.models.menu import Menu

# TODO update the JSON string below
json = "{}"
# create an instance of Menu from a JSON string
menu_instance = Menu.from_json(json)
# print the JSON string representation of the object
print(Menu.to_json())

# convert the object into a dict
menu_dict = menu_instance.to_dict()
# create an instance of Menu from a dict
menu_from_dict = Menu.from_dict(menu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


