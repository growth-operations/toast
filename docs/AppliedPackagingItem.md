# AppliedPackagingItem

Indicates the guest preference for an individual packaging item in this order. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**item_config_id** | **str** | The identifier GUID of the packaging preference option.  | 
**inclusion** | **str** | The packaging preference choice that the guest selected in your ordering interface.  | 
**item_types** | **List[str]** | The packaging item types relevant for this packaging item as configured by the restaurant in Toast Web. Response only.  | [optional] 
**guest_display_name** | **str** | The guest-facing name, configured by the restaurant in Toast Web, for this packaging item. Response only.  | [optional] 

## Example

```python
from toastapi.models.applied_packaging_item import AppliedPackagingItem

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedPackagingItem from a JSON string
applied_packaging_item_instance = AppliedPackagingItem.from_json(json)
# print the JSON string representation of the object
print(AppliedPackagingItem.to_json())

# convert the object into a dict
applied_packaging_item_dict = applied_packaging_item_instance.to_dict()
# create an instance of AppliedPackagingItem from a dict
applied_packaging_item_from_dict = AppliedPackagingItem.from_dict(applied_packaging_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


