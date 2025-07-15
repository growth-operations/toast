# PortionV2

A container for the modifier groups that can be applied to a portion of a menu item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this portion, for example, \&quot;1st Half\&quot; or \&quot;2nd Half\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this portion, assigned by the Toast POS system.  | [optional] 
**modifier_group_references** | **List[int]** | An array of &#x60;referenceId&#x60;s for &#x60;ModifierGroup&#x60; objects. These objects define the modifier groups that can be applied to this portion.  | [optional] 

## Example

```python
from toastapi.models.portion_v2 import PortionV2

# TODO update the JSON string below
json = "{}"
# create an instance of PortionV2 from a JSON string
portion_v2_instance = PortionV2.from_json(json)
# print the JSON string representation of the object
print(PortionV2.to_json())

# convert the object into a dict
portion_v2_dict = portion_v2_instance.to_dict()
# create an instance of PortionV2 from a dict
portion_v2_from_dict = PortionV2.from_dict(portion_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


