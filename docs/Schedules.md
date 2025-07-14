# Schedules

Information about the services and hours that are scheduled for a restaurant during different types of days. For example, a restaurant might have different services available on weekdays than it does on weekends. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**week_schedule** | [**WeekSchedule**](WeekSchedule.md) |  | [optional] 
**day_schedules** | [**Dict[str, DaySchedule]**](DaySchedule.md) | A map of &#x60;DaySchedule&#x60; objects that define the services and hours for different types of days. Each &#x60;DaySchedule&#x60; object is presented as a key/value pair. A pair&#39;s key matches the &#x60;scheduleName&#x60; of the object contained in the pair&#39;s value.  | [optional] 

## Example

```python
from toastapi.models.schedules import Schedules

# TODO update the JSON string below
json = "{}"
# create an instance of Schedules from a JSON string
schedules_instance = Schedules.from_json(json)
# print the JSON string representation of the object
print(Schedules.to_json())

# convert the object into a dict
schedules_dict = schedules_instance.to_dict()
# create an instance of Schedules from a dict
schedules_from_dict = Schedules.from_dict(schedules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


