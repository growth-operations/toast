# BreakType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**name** | **str** | The name of the work break type, as recognized by restaurant employees.  | [optional] 
**active** | **bool** | Indicates whether the break is available and can be taken by restaurant employees.  | [optional] 
**paid** | **bool** | Indicates whether the break is paid. | [optional] 
**duration** | **int** | The duration of the break in minutes. | [optional] 
**enforce_minimum_time** | **bool** | Indicates whether the duration is enforced as the minimum time for the break.  | [optional] 
**track_missed_breaks** | **bool** | True if breaks that are not taken within the specified break interval should be generated in Toast.  | [optional] 
**break_interval_hrs** | **int** | The number of hours between break intervals. Break intervals are specified in hours and minutes. If missed breaks are not tracked, this value may be null.  | [optional] 
**break_interval_mins** | **int** | The number of minutes between break intervals. Break intervals are specified in hours and minutes. If missed breaks are not tracked, this value may be null.  | [optional] 
**track_break_acknowledgement** | **bool** | Indicates whether break acknowledgements are collected for this type of break. Break acknowledgements will not be collected if &#x60;trackMissedBreaks&#x60; is false.  | [optional] 

## Example

```python
from toastapi.models.break_type import BreakType

# TODO update the JSON string below
json = "{}"
# create an instance of BreakType from a JSON string
break_type_instance = BreakType.from_json(json)
# print the JSON string representation of the object
print(BreakType.to_json())

# convert the object into a dict
break_type_dict = break_type_instance.to_dict()
# create an instance of BreakType from a dict
break_type_from_dict = BreakType.from_dict(break_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


