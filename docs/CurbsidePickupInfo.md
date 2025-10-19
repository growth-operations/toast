# CurbsidePickupInfo

Information that the restaurant can use to identify a guest when they arrive outside the restaurant to pick up their order. `transportDescription` is a required field. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**transport_color** | **str** | The color of the guest&#39;s vehicle if they will arrive at the restaurant in a vehicle to pick up their order.  | [optional] 
**transport_description** | **str** | Information about how the guest will arrive at the restaurant to pick up their order.  For example, the make and model of the vehicle the guest will arrive in.  | [optional] 

## Example

```python
from toastapi.models.curbside_pickup_info import CurbsidePickupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CurbsidePickupInfo from a JSON string
curbside_pickup_info_instance = CurbsidePickupInfo.from_json(json)
# print the JSON string representation of the object
print(CurbsidePickupInfo.to_json())

# convert the object into a dict
curbside_pickup_info_dict = curbside_pickup_info_instance.to_dict()
# create an instance of CurbsidePickupInfo from a dict
curbside_pickup_info_from_dict = CurbsidePickupInfo.from_dict(curbside_pickup_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


