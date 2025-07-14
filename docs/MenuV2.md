# MenuV2

Information about a menu configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this menu, for example, \&quot;Food\&quot; or \&quot;Drinks\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this menu, assigned by the Toast POS system.  | [optional] 
**multi_location_id** | **str** | An identifier that is used to identify and consolidate menu entities that are versions of each other. | [optional] 
**master_id** | **int** | This value is deprecated. Instead of masterId, use multiLocationId. | [optional] 
**description** | **str** | An optional short description for this menu.  | [optional] 
**pos_name** | **str** | The button label name that appears for this menu entity in the Toast POS app. | [optional] 
**pos_button_color_light** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in light mode. | [optional] 
**pos_button_color_dark** | **str** | The color of the menu entity&#39;s button on the Toast POS app, when the app is running in dark mode. | [optional] 
**high_res_image** | **str** | The URL to a high resolution image that has been uploaded for this menu. The image file must be in JPG, PNG, or SVG format. The &#x60;highResImage&#x60; value is only available if the Toast Kiosk module has been enabled for this restaurant. This value is null if no high resolution image has been specified.  | [optional] 
**image** | **str** | The URL to an image that has been uploaded for this menu entity. | [optional] 
**visibility** | **List[str]** | An array of strings that indicate where this menu entity is visible. | [optional] 
**availability** | [**MenuV2Availability**](MenuV2Availability.md) |  | [optional] 
**menu_groups** | [**List[MenuGroupV2]**](MenuGroupV2.md) | An array of the &#x60;MenuGroup&#x60; objects contained in this menu.  | [optional] 

## Example

```python
from toastapi.models.menu_v2 import MenuV2

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV2 from a JSON string
menu_v2_instance = MenuV2.from_json(json)
# print the JSON string representation of the object
print(MenuV2.to_json())

# convert the object into a dict
menu_v2_dict = menu_v2_instance.to_dict()
# create an instance of MenuV2 from a dict
menu_v2_from_dict = MenuV2.from_dict(menu_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


