# Selection

A `Selection` object can represent either a primary item or a modifier selection. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**item** | **object** |  | 
**item_group** | **object** |  | [optional] 
**option_group** | **object** |  | [optional] 
**quantity** | **float** | Quantity ordered. | 
**seat_number** | **int** | Indicates which guest seat at a restaurant table ordered a menu item selection.  | [optional] 
**price** | **float** | The price of this selection. | [optional] 
**voided** | **bool** | True if this selection is voided. | [optional] 
**void_date** | **datetime** | The date when this selection was voided. | [optional] 
**modifiers** | [**List[Selection]**](Selection.md) | Modifier selections for this item. | [optional] 

## Example

```python
from toastapi.models.selection import Selection

# TODO update the JSON string below
json = "{}"
# create an instance of Selection from a JSON string
selection_instance = Selection.from_json(json)
# print the JSON string representation of the object
print(Selection.to_json())

# convert the object into a dict
selection_dict = selection_instance.to_dict()
# create an instance of Selection from a dict
selection_from_dict = Selection.from_dict(selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


