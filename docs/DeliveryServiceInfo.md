# DeliveryServiceInfo

Reserved for future use. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**provider_id** | **str** | Reserved for future use.  | [optional] 
**provider_name** | **str** | Reserved for future use.  | [optional] 
**driver_name** | **str** | Reserved for future use.  | [optional] 
**driver_phone_number** | **str** | Reserved for future use.  | [optional] 
**provider_info** | **bytearray** | Reserved for future use.  | [optional] 
**original_quoted_delivery_date** | **str** | Reserved for future use.  | [optional] 

## Example

```python
from toastapi.models.delivery_service_info import DeliveryServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryServiceInfo from a JSON string
delivery_service_info_instance = DeliveryServiceInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveryServiceInfo.to_json())

# convert the object into a dict
delivery_service_info_dict = delivery_service_info_instance.to_dict()
# create an instance of DeliveryServiceInfo from a dict
delivery_service_info_from_dict = DeliveryServiceInfo.from_dict(delivery_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


