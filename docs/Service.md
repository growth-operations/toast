# Service

A time-based division of the operation of the restaurant. For example, a service might be named `lunch` and it might be available between specific hours during the day. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**hours** | [**Hours**](Hours.md) |  | [optional] 
**overnight** | **bool** | Indicates whether any portion of the period of time that a service is available occurs after 00:00 (midnight) and before the business day cutoff time for the restaurant which is  available in the &#x60;closeoutHour&#x60; property. An overnight shift spans two calendar dates but occurs during one business day.  | [optional] 

## Example

```python
from toastapi.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


