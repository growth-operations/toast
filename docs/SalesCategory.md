# SalesCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**name** | **str** | The name of this sales category. | [optional] 

## Example

```python
from toastapi.models.sales_category import SalesCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SalesCategory from a JSON string
sales_category_instance = SalesCategory.from_json(json)
# print the JSON string representation of the object
print(SalesCategory.to_json())

# convert the object into a dict
sales_category_dict = sales_category_instance.to_dict()
# create an instance of SalesCategory from a dict
sales_category_from_dict = SalesCategory.from_dict(sales_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


