# Shift

A scheduled shift in the Toast platform used to enforce employee  clock-in and clock outs. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**created_date** | **datetime** | Date created, in UTC format (read-only).  | [optional] 
**modified_date** | **datetime** | Date modified, in UTC format (read-only).  | [optional] 
**deleted** | **bool** | If the shift is deleted in the Toast platform.  | [optional] 
**job_reference** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**employee_reference** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**in_date** | **datetime** | Timestamp of the beginning of the shift. This is when the  employee can clock in. Expressed in the UTC time zone.  | [optional] 
**out_date** | **datetime** | Timestamp of the end of the shift. This is when the  employee can clock out. Expressed in the UTC time zone.  | [optional] 

## Example

```python
from toastapi.models.shift import Shift

# TODO update the JSON string below
json = "{}"
# create an instance of Shift from a JSON string
shift_instance = Shift.from_json(json)
# print the JSON string representation of the object
print(Shift.to_json())

# convert the object into a dict
shift_dict = shift_instance.to_dict()
# create an instance of Shift from a dict
shift_from_dict = Shift.from_dict(shift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


