# Device

The *Device ID* value that the Toast platform assigns to a specific Toast POS device.  The `id` value is a unique identifier for a device.  To find the ID for a Toast POS device, from the overflow  menu (⋮) select *Device Status* and then select the *Device* tab. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The physical id of the device | [optional] 

## Example

```python
from toastapi.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


