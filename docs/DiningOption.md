# DiningOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**name** | **str** | The name of the dining option. | [optional] 
**behavior** | **str** | The behavior of the dining option. &#x60;TAKE_OUT&#x60; and &#x60;DELIVERY&#x60; require a &#x60;customer&#x60; to be specified on the order, and &#x60;DELIVERY&#x60; requires a &#x60;deliveryInfo&#x60; value.  | [optional] 
**curbside** | **bool** | Indicates whether the dining option has curbside behavior, and allows the guest to provide identifying information such as a description of their vehicle.  | [optional] 

## Example

```python
from toastapi.models.dining_option import DiningOption

# TODO update the JSON string below
json = "{}"
# create an instance of DiningOption from a JSON string
dining_option_instance = DiningOption.from_json(json)
# print the JSON string representation of the object
print(DiningOption.to_json())

# convert the object into a dict
dining_option_dict = dining_option_instance.to_dict()
# create an instance of DiningOption from a dict
dining_option_from_dict = DiningOption.from_dict(dining_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


