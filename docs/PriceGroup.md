# PriceGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**name** | **str** | The name of this price group. | [optional] 

## Example

```python
from toastapi.models.price_group import PriceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PriceGroup from a JSON string
price_group_instance = PriceGroup.from_json(json)
# print the JSON string representation of the object
print(PriceGroup.to_json())

# convert the object into a dict
price_group_dict = price_group_instance.to_dict()
# create an instance of PriceGroup from a dict
price_group_from_dict = PriceGroup.from_dict(price_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


