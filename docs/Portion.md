# Portion

Information about a portion that can be defined for menu items and modifier options. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | A unique identifier for this portion. | [optional] 
**name** | **str** | The name of this portion. | [optional] 

## Example

```python
from toastapi.models.portion import Portion

# TODO update the JSON string below
json = "{}"
# create an instance of Portion from a JSON string
portion_instance = Portion.from_json(json)
# print the JSON string representation of the object
print(Portion.to_json())

# convert the object into a dict
portion_dict = portion_instance.to_dict()
# create an instance of Portion from a dict
portion_from_dict = Portion.from_dict(portion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


