# Schedule

A multi-use object that is used to:  * Define when a menu is available. * Define when a time-specific price is available for a menu item or modifier option.  A `Schedule` object defines a set of days of the week and a set of time ranges for those days. Days that have identical time ranges are grouped into a single `Schedule` object.  Time ranges are in 24-hour HH:MM format.  If a day is not represented in the `Schedule` objects, the menu or time-specific price is not available on that day. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **List[str]** | An array of strings that represent the days of the week when this schedule is active.  | [optional] 
**time_ranges** | [**List[TimeRange]**](TimeRange.md) | An array of time range objects that define the specific time periods for the days specified in the &#x60;days&#x60; array.  | [optional] 

## Example

```python
from toastapi.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print(Schedule.to_json())

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_from_dict = Schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


