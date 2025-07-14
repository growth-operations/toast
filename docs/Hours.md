# Hours

The period of time that the restaurant offers a service. For example, a service might be named \"lunch\" and it might be offered between `10:00:00.000` and `16:00:00.000`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | The time of day that the service begins. | [optional] 
**end_time** | **str** | The time of day that the service ends. | [optional] 

## Example

```python
from toastapi.models.hours import Hours

# TODO update the JSON string below
json = "{}"
# create an instance of Hours from a JSON string
hours_instance = Hours.from_json(json)
# print the JSON string representation of the object
print(Hours.to_json())

# convert the object into a dict
hours_dict = hours_instance.to_dict()
# create an instance of Hours from a dict
hours_from_dict = Hours.from_dict(hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


