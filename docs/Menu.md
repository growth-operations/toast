# Menu

Information about a menu configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this menu, for example, \&quot;Food\&quot; or \&quot;Drinks\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this menu, assigned by the Toast POS system.  | [optional] 
**description** | **str** | An optional short description for this menu.  | [optional] 
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


