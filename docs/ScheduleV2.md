# ScheduleV2

A multi-use object that defines when a menu is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **List[str]** | An array of days of the week. | [optional] 
**time_ranges** | [**List[TimeRangeV2]**](TimeRangeV2.md) | An array of TimeRange objects. | [optional] 

## Example

```python
from toastapi.models.schedule_v2 import ScheduleV2

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleV2 from a JSON string
schedule_v2_instance = ScheduleV2.from_json(json)
# print the JSON string representation of the object
print(ScheduleV2.to_json())

# convert the object into a dict
schedule_v2_dict = schedule_v2_instance.to_dict()
# create an instance of ScheduleV2 from a dict
schedule_v2_from_dict = ScheduleV2.from_dict(schedule_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


