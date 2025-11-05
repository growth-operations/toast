# TaxRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**name** | **str** | The name of this tax rate. | [optional] 
**is_default** | **bool** | True if this tax rate is the default tax rate. | [optional] 
**rate** | **float** | The tax rate value.  | [optional] 
**rounding_type** | **str** | The method used to round fractional currency amounts to non-fractional currency amounts.  Only applies to PERCENT tax rates. For other tax rate types, roundingType is null.  Valid values: HALF_UP - Round values up or down to the nearest number. If the last digit is 5, which is halfway, then always round up to the nearest number. HALF_EVEN - Round values up or down to the nearest number. If the last digit is 5, which is halfway, then round up or down to the nearest even number. ALWAYS_UP - Always round up to the next number. ALWAYS_DOWN - Always round down to the next number.  | [optional] 
**tax_table** | [**List[TaxTableRow]**](TaxTableRow.md) | An array of TaxTableRow objects that define a set of tax amounts that apply to specific sale amount ranges. | [optional] 
**type** | **str** | The type of tax rate. | [optional] 

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


