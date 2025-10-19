# MenuOptionGroup

Information about a modifier group (option group) configured for a restaurant. For example, salad dressings might be a modifier group for a salad menu item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**name** | **str** | The name of the menu option group as it appears in the Toast POS.  | [optional] 
**options** | [**List[ExternalReference]**](ExternalReference.md) | An array of ExternalReference objects containing the identifiers of the menu items (modifiers) in the menu option group.  | [optional] 
**min_selections** | **float** | The minimum number of selections that must be made from this option group.  | [optional] 
**max_selections** | **float** | The maximum number of selections that can be made from this option group.  | [optional] 

## Example

```python
from toastapi.models.menu_option_group import MenuOptionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MenuOptionGroup from a JSON string
menu_option_group_instance = MenuOptionGroup.from_json(json)
# print the JSON string representation of the object
print(MenuOptionGroup.to_json())

# convert the object into a dict
menu_option_group_dict = menu_option_group_instance.to_dict()
# create an instance of MenuOptionGroup from a dict
menu_option_group_from_dict = MenuOptionGroup.from_dict(menu_option_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


