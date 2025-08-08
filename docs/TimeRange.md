# TimeRange

Defines a time range with start and end times in 24-hour HH:MM format. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | The start time in 24-hour HH:MM format (e.g., \&quot;09:00\&quot;).  | [optional] 
**end** | **str** | The end time in 24-hour HH:MM format (e.g., \&quot;18:00\&quot;).  | [optional] 

## Example

```python
from toastapi.models.time_range import TimeRange

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRange from a JSON string
time_range_instance = TimeRange.from_json(json)
# print the JSON string representation of the object
print(TimeRange.to_json())

# convert the object into a dict
time_range_dict = time_range_instance.to_dict()
# create an instance of TimeRange from a dict
time_range_from_dict = TimeRange.from_dict(time_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


