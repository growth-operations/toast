# DaySchedule

Information about the services and hours that are scheduled for a restaurant during a type of day. For example, a restaurant might have different services available on a type of day named `weekday` than it does on a type of day named `weekend`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_name** | **str** | The name of the type of day. For example, &#x60;weekday&#x60;. | [optional] 
**services** | [**List[Service]**](Service.md) | An array of &#x60;Service&#x60; objects that are available during the type of day.  | [optional] 
**open_time** | **str** | The time of day that the first service for the type of day begins. For example, the first service might begin at &#x60;06:00:00.000&#x60;.  | [optional] 
**close_time** | **str** | The time of day that the last service for the type of day ends. For example, the last service might end at &#x60;02:00:00.000&#x60;.  | [optional] 

## Example

```python
from toastapi.models.day_schedule import DaySchedule

# TODO update the JSON string below
json = "{}"
# create an instance of DaySchedule from a JSON string
day_schedule_instance = DaySchedule.from_json(json)
# print the JSON string representation of the object
print(DaySchedule.to_json())

# convert the object into a dict
day_schedule_dict = day_schedule_instance.to_dict()
# create an instance of DaySchedule from a dict
day_schedule_from_dict = DaySchedule.from_dict(day_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


