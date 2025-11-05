# TaxTableRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **float** | The end of a sale amount range that corresponds to a specific tax amount in a tax table. | [optional] 
**pattern** | **str** | Specifies whether the price range is part of an incomplete set of ranges that establish an algorithm that you can use to calculate tax amounts. | [optional] 
**start** | **float** | The start of a sale amount range that corresponds to a specific tax amount in a tax table. | [optional] 
**tax** | **float** | The tax amount that applies to the sale amount range. | [optional] 

## Example

```python
from toastapi.models.tax_table_row import TaxTableRow

# TODO update the JSON string below
json = "{}"
# create an instance of TaxTableRow from a JSON string
tax_table_row_instance = TaxTableRow.from_json(json)
# print the JSON string representation of the object
print(TaxTableRow.to_json())

# convert the object into a dict
tax_table_row_dict = tax_table_row_instance.to_dict()
# create an instance of TaxTableRow from a dict
tax_table_row_from_dict = TaxTableRow.from_dict(tax_table_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


