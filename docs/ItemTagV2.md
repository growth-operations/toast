# ItemTagV2

A descriptive term that identifies a characteristic of a menu item or menu group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this item tag. | [optional] 
**guid** | **str** | A unique identifier for this item tag. | [optional] 

## Example

```python
from toastapi.models.item_tag_v2 import ItemTagV2

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTagV2 from a JSON string
item_tag_v2_instance = ItemTagV2.from_json(json)
# print the JSON string representation of the object
print(ItemTagV2.to_json())

# convert the object into a dict
item_tag_v2_dict = item_tag_v2_instance.to_dict()
# create an instance of ItemTagV2 from a dict
item_tag_v2_from_dict = ItemTagV2.from_dict(item_tag_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


