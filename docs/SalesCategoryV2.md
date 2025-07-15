# SalesCategoryV2

A descriptive category, for example, \"Food\" or \"Liquor\" that, when applied to the menu items and modifier options in your menu, allow you to view sales data by category. Null if no sales category has been defined. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this sales category, for example, \&quot;Food\&quot; or \&quot;Liquor\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this sales category, assigned by the Toast POS system.  | [optional] 

## Example

```python
from toastapi.models.sales_category_v2 import SalesCategoryV2

# TODO update the JSON string below
json = "{}"
# create an instance of SalesCategoryV2 from a JSON string
sales_category_v2_instance = SalesCategoryV2.from_json(json)
# print the JSON string representation of the object
print(SalesCategoryV2.to_json())

# convert the object into a dict
sales_category_v2_dict = sales_category_v2_instance.to_dict()
# create an instance of SalesCategoryV2 from a dict
sales_category_v2_from_dict = SalesCategoryV2.from_dict(sales_category_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


