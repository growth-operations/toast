# RevenueCenter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**name** | **str** | The name of this revenue center. | [optional] 
**description** | **str** | The description of this revenue center. | [optional] 

## Example

```python
from toastapi.models.revenue_center import RevenueCenter

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueCenter from a JSON string
revenue_center_instance = RevenueCenter.from_json(json)
# print the JSON string representation of the object
print(RevenueCenter.to_json())

# convert the object into a dict
revenue_center_dict = revenue_center_instance.to_dict()
# create an instance of RevenueCenter from a dict
revenue_center_from_dict = RevenueCenter.from_dict(revenue_center_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


