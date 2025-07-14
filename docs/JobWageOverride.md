# JobWageOverride

The overriding job wage, for an employee that has a wage that  differs from the job's default wage. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wage** | **float** | Required currency value of the employee&#39;s overriding job wage.  | 
**job_reference** | [**ExternalReference**](.md) |  | 

## Example

```python
from toastapi.models.job_wage_override import JobWageOverride

# TODO update the JSON string below
json = "{}"
# create an instance of JobWageOverride from a JSON string
job_wage_override_instance = JobWageOverride.from_json(json)
# print the JSON string representation of the object
print(JobWageOverride.to_json())

# convert the object into a dict
job_wage_override_dict = job_wage_override_instance.to_dict()
# create an instance of JobWageOverride from a dict
job_wage_override_from_dict = JobWageOverride.from_dict(job_wage_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


