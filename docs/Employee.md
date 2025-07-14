# Employee

A restaurant employee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**created_date** | **datetime** | Date created, in UTC format (read-only).  | [optional] 
**modified_date** | **datetime** | Date modified, in UTC format (read-only).  | [optional] 
**first_name** | **str** | Optional, first name of the employee.  | [optional] 
**chosen_name** | **str** | Optional, chosen name of the employee.  | [optional] 
**last_name** | **str** | Optional, last name of the employee.  | [optional] 
**email** | **str** | Employee&#39;s email address.  | [optional] 
**phone_number** | **str** | Employee&#39;s phone number  | [optional] 
**passcode** | **str** | An optional numeric security code that a new employee can  use to begin a session in a Toast POS device.  | [optional] 
**external_employee_id** | **str** | Optional, employee&#39;s external ID in the Toast platform.  | [optional] 
**deleted** | **bool** | If the employee is deleted in the Toast platform.  | [optional] 
**job_references** | [**List[ExternalReference]**](ExternalReference.md) | An array of external references to jobs assigned to this  employee.  | [optional] 
**wage_overrides** | [**List[JobWageOverride]**](JobWageOverride.md) | An optional array of per job wage overrides.  | [optional] 

## Example

```python
from toastapi.models.employee import Employee

# TODO update the JSON string below
json = "{}"
# create an instance of Employee from a JSON string
employee_instance = Employee.from_json(json)
# print the JSON string representation of the object
print(Employee.to_json())

# convert the object into a dict
employee_dict = employee_instance.to_dict()
# create an instance of Employee from a dict
employee_from_dict = Employee.from_dict(employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


