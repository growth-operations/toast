# TaxRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**name** | **str** | The name of this tax rate. | [optional] 
**is_default** | **bool** | True if this tax rate is the default tax rate. | [optional] 
**rate** | **float** | The tax rate value.  | [optional] 

## Example

```python
from toastapi.models.tax_rate import TaxRate

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRate from a JSON string
tax_rate_instance = TaxRate.from_json(json)
# print the JSON string representation of the object
print(TaxRate.to_json())

# convert the object into a dict
tax_rate_dict = tax_rate_instance.to_dict()
# create an instance of TaxRate from a dict
tax_rate_from_dict = TaxRate.from_dict(tax_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


