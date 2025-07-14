# TimeEntryBreak

Information about a period of time that an employee is not working during a shift. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform.  | [optional] 
**break_type** | [**ToastReference**](.md) |  | [optional] 
**paid** | **bool** | Indicates whether the employee was paid for the break.  | [optional] 
**in_date** | **datetime** | The date and time that the employee started the break period, in UTC.  | [optional] 
**out_date** | **datetime** | The date and time that the employee ended the break period and returned to work, in UTC.  | [optional] 
**missed** | **bool** | Indicates whether the break was a missed break.  | [optional] 

## Example

```python
from toastapi.models.time_entry_break import TimeEntryBreak

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntryBreak from a JSON string
time_entry_break_instance = TimeEntryBreak.from_json(json)
# print the JSON string representation of the object
print(TimeEntryBreak.to_json())

# convert the object into a dict
time_entry_break_dict = time_entry_break_instance.to_dict()
# create an instance of TimeEntryBreak from a dict
time_entry_break_from_dict = TimeEntryBreak.from_dict(time_entry_break_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


