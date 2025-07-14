# WeekSchedule

The day schedule used for each day of the week. A day schedule is  the set of services (for example, \"lunch\") that a restaurant  offers and the hours that it offers each one. If a day of the  week value in this object is `null`, the restaurant is closed on  that day. Values for each day of the week are identifiers for day  schedules in the map of `DaySchedule` objects in the  `daySchedules` value of the `Schedules` object. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monday** | **str** | A key identifier for the &#x60;DaySchedule&#x60; object that represents the services and hours for the restaurant on this day of the week.  | [optional] 
**tuesday** | **str** | A key identifier for the &#x60;DaySchedule&#x60; object that represents the services and hours for the restaurant on this day of the week.  | [optional] 
**wednesday** | **str** | A key identifier for the &#x60;DaySchedule&#x60; object that represents the services and hours for the restaurant on this day of the week.  | [optional] 
**thursday** | **str** | A key identifier for the &#x60;DaySchedule&#x60; object that represents the services and hours for the restaurant on this day of the week.  | [optional] 
**friday** | **str** | A key identifier for the &#x60;DaySchedule&#x60; object that represents the services and hours for the restaurant on this day of the week.  | [optional] 
**saturday** | **str** | A key identifier for the &#x60;DaySchedule&#x60; object that represents the services and hours for the restaurant on this day of the week.  | [optional] 
**sunday** | **str** | A key identifier for the &#x60;DaySchedule&#x60; object that represents the services and hours for the restaurant on this day of the week.  | [optional] 

## Example

```python
from toastapi.models.week_schedule import WeekSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of WeekSchedule from a JSON string
week_schedule_instance = WeekSchedule.from_json(json)
# print the JSON string representation of the object
print(WeekSchedule.to_json())

# convert the object into a dict
week_schedule_dict = week_schedule_instance.to_dict()
# create an instance of WeekSchedule from a dict
week_schedule_from_dict = WeekSchedule.from_dict(week_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


