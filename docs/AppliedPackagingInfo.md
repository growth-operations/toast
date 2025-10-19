# AppliedPackagingInfo

Information describing the guest's packaging preferences for this order, for example utensils, napkins, condiments.  For more information, see <a href=\"https://doc.toasttab.com/doc/devguide/apiOrdersPackagingPreferences.html\">Packaging preferences</a> 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**applied_packaging_items** | [**List[AppliedPackagingItem]**](AppliedPackagingItem.md) |  | [optional] 

## Example

```python
from toastapi.models.applied_packaging_info import AppliedPackagingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedPackagingInfo from a JSON string
applied_packaging_info_instance = AppliedPackagingInfo.from_json(json)
# print the JSON string representation of the object
print(AppliedPackagingInfo.to_json())

# convert the object into a dict
applied_packaging_info_dict = applied_packaging_info_instance.to_dict()
# create an instance of AppliedPackagingInfo from a dict
applied_packaging_info_from_dict = AppliedPackagingInfo.from_dict(applied_packaging_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


