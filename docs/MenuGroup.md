# MenuGroup

Information about a menu group configured for this restaurant, including an array of menu items contained in the group. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this menu group, for example, \&quot;Appetizers\&quot; or \&quot;Sandwiches\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this menu group, assigned by the Toast POS system.  | [optional] 
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


