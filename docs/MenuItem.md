# MenuItem

Information about a menu item configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this menu item.  | [optional] 
**guid** | **str** | A unique identifier for this menu item, assigned by the Toast POS system.  | [optional] 
**price** | **float** | The price of this menu item.  | [optional] 

## Example

```python
from toastapi.models.menu_item import MenuItem

# TODO update the JSON string below
json = "{}"
# create an instance of MenuItem from a JSON string
menu_item_instance = MenuItem.from_json(json)
# print the JSON string representation of the object
print(MenuItem.to_json())

# convert the object into a dict
menu_item_dict = menu_item_instance.to_dict()
# create an instance of MenuItem from a dict
menu_item_from_dict = MenuItem.from_dict(menu_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


