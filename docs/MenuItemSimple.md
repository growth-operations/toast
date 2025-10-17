# MenuItemSimple

Simplified menu item information returned by config/v2/menuItems endpoints. This schema contains a subset of the full MenuItem properties with simpler structure. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | A unique identifier for this menu item, assigned by the Toast POS system.  | [optional] 
**entity_type** | **str** | The type of entity. Always \&quot;MenuItem\&quot; for menu items.  | [optional] 
**external_id** | **str** | An external identifier for this menu item, if configured.  | [optional] 
**inherit_unit_of_measure** | **bool** | Indicates whether this menu item inherits its unit of measure from a parent entity.  | [optional] 
**images** | **List[str]** | An array of image URLs or references for this menu item.  | [optional] 
**inherit_option_groups** | **bool** | Indicates whether this menu item inherits its option groups from a parent entity.  | [optional] 
**visibility** | **str** | A string that represents where this menu item is visible. Possible values include ALL, POS, KIOSK, TOAST_ONLINE_ORDERING, ORDERING_PARTNERS, GRUBHUB.  | [optional] 
**unit_of_measure** | **str** | The unit of measure used to determine the price of the item. For example, $10.00 per gram.  | [optional] 
**orderable_online** | **str** | Indicates whether this menu item can be ordered online. Possible values include \&quot;Yes\&quot;, \&quot;No\&quot;.  | [optional] 
**name** | **str** | A descriptive name for this menu item, for example, \&quot;Caesar Salad\&quot; or \&quot;Turkey Sandwich\&quot;.  | [optional] 
**plu** | **str** | The price lookup (PLU) code for this menu item. The PLU code can include both numbers and letters. This value contains an empty string if a PLU code has not been defined.  | [optional] 
**option_groups** | **List[object]** | An array of option group references for this menu item.  | [optional] 
**calories** | **int** | The number of calories in this menu item. The calories value can be any positive or negative integer, or zero. This value is null if a calories amount has not been configured for the menu item.  | [optional] 
**sku** | **str** | The stock keeping unit (SKU) identifier for this menu item. The SKU identifier can include both numbers and letters. This value is null if a SKU has not been defined.  | [optional] 
**type** | **str** | The type classification of this menu item, if configured.  | [optional] 

## Example

```python
from toastapi.models.menu_item_simple import MenuItemSimple

# TODO update the JSON string below
json = "{}"
# create an instance of MenuItemSimple from a JSON string
menu_item_simple_instance = MenuItemSimple.from_json(json)
# print the JSON string representation of the object
print(MenuItemSimple.to_json())

# convert the object into a dict
menu_item_simple_dict = menu_item_simple_instance.to_dict()
# create an instance of MenuItemSimple from a dict
menu_item_simple_from_dict = MenuItemSimple.from_dict(menu_item_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


