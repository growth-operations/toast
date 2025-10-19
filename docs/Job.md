# Job

A restaurant job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**created_date** | **datetime** | Date created, in UTC format (read-only).  | [optional] 
**modified_date** | **datetime** | Date modified, in UTC format (read-only).  | [optional] 
**title** | **str** | Title of the job.  | [optional] 
**deleted** | **bool** | If the job is deleted in the Toast platform.  | [optional] 
**wage_frequency** | **str** | An enumerated type specifying how to interpret the  default wage for this job.  | [optional] 
**default_wage** | **float** | The default wage of the job.  | [optional] 
**tipped** | **bool** | Indicates whether the job receives gratuities (tips).  | [optional] 
**code** | **str** | A reference identifier for the job.  | [optional] 

## Example

```python
from toastapi.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


