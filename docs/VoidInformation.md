# VoidInformation

Information about a void applied to a check or item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**void_user** | [**ExternalReference**](.md) |  | [optional] 
**void_approver** | [**ExternalReference**](.md) |  | [optional] 
**void_date** | **datetime** | The date on which the void was made. | [optional] 
**void_business_date** | **int** | The business date (yyyyMMdd) on which the void was made. Response only. | [optional] 
**void_reason** | [**ExternalReference**](.md) |  | [optional] 

## Example

```python
from toastapi.models.void_information import VoidInformation

# TODO update the JSON string below
json = "{}"
# create an instance of VoidInformation from a JSON string
void_information_instance = VoidInformation.from_json(json)
# print the JSON string representation of the object
print(VoidInformation.to_json())

# convert the object into a dict
void_information_dict = void_information_instance.to_dict()
# create an instance of VoidInformation from a dict
void_information_from_dict = VoidInformation.from_dict(void_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


