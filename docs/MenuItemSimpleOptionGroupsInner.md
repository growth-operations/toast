# MenuItemSimpleOptionGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID of the option group. | [optional] 
**entity_type** | **str** | The type of entity, typically \&quot;MenuOptionGroup\&quot;. | [optional] 
**external_id** | **str** | External identifier for the option group, if configured. | [optional] 

## Example

```python
from toastapi.models.menu_item_simple_option_groups_inner import MenuItemSimpleOptionGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MenuItemSimpleOptionGroupsInner from a JSON string
menu_item_simple_option_groups_inner_instance = MenuItemSimpleOptionGroupsInner.from_json(json)
# print the JSON string representation of the object
print(MenuItemSimpleOptionGroupsInner.to_json())

# convert the object into a dict
menu_item_simple_option_groups_inner_dict = menu_item_simple_option_groups_inner_instance.to_dict()
# create an instance of MenuItemSimpleOptionGroupsInner from a dict
menu_item_simple_option_groups_inner_from_dict = MenuItemSimpleOptionGroupsInner.from_dict(menu_item_simple_option_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


