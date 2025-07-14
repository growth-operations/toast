# TimeRangeV2

Represents a time range for when a menu is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | The start time of the time range. | [optional] 
**end** | **str** | The end time of the time range. | [optional] 

## Example

```python
from toastapi.models.time_range_v2 import TimeRangeV2

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRangeV2 from a JSON string
time_range_v2_instance = TimeRangeV2.from_json(json)
# print the JSON string representation of the object
print(TimeRangeV2.to_json())

# convert the object into a dict
time_range_v2_dict = time_range_v2_instance.to_dict()
# create an instance of TimeRangeV2 from a dict
time_range_v2_from_dict = TimeRangeV2.from_dict(time_range_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


