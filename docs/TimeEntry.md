# TimeEntry

A `TimeEntry` captures the actual time an employee worked or took  a break. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**created_date** | **datetime** | Date created, in UTC format (read-only).  | [optional] 
**modified_date** | **datetime** | Date modified, in UTC format (read-only).  | [optional] 
**deleted** | **bool** | If the time entry is deleted in the Toast platform.  | [optional] 
**job_reference** | **object** |  | [optional] 
**employee_reference** | **object** |  | [optional] 
**shift_reference** | **object** |  | [optional] 
**in_date** | **datetime** | The date and time that an employee clocked in to a work shift.  | [optional] 
**out_date** | **datetime** | The date and time that an employee closed a work shift.  | [optional] 
**auto_clocked_out** | **bool** | Indicates whether the Toast platform automatically clocked the employee out of their shift at the end of the restaurant business day.  | [optional] 
**business_date** | **str** | The business date of &#x60;inDate&#x60;, in the format of  \&quot;yyyymmdd\&quot;.  | [optional] 
**regular_hours** | **float** | Regular hours worked by the employee for this time entry,  excluding breaks.  | [optional] 
**overtime_hours** | **float** | Any overtime hours taken by this employee during this  time entry.  | [optional] 
**hourly_wage** | **float** | Optional, historical &#x60;hourlyWage&#x60;; that is, the wage in  effect when the time entry was made.  | [optional] 
**breaks** | [**List[TimeEntryBreak]**](TimeEntryBreak.md) | An optional array of time entry breaks, each break  defining a clock-in date, clock-out date, and whether or  not the break was paid.  | [optional] 
**declared_cash_tips** | **float** | The currency amount of tips paid in cash during the time entry.  | [optional] 
**non_cash_tips** | **float** | The currency amount of tips paid using non-cash tender during the time entry.  | [optional] 

## Example

```python
from toastapi.models.time_entry import TimeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntry from a JSON string
time_entry_instance = TimeEntry.from_json(json)
# print the JSON string representation of the object
print(TimeEntry.to_json())

# convert the object into a dict
time_entry_dict = time_entry_instance.to_dict()
# create an instance of TimeEntry from a dict
time_entry_from_dict = TimeEntry.from_dict(time_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


