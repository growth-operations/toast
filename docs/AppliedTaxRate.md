# AppliedTaxRate

A tax rate that is applied to an item or service charge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. | 
**tax_rate** | **object** |  | 
**name** | **str** | The name of the tax rate. | [optional] 
**rate** | **float** | The tax rate, which can be a fixed amount, a percentage, or null. | [optional] 
**tax_amount** | **float** | The tax amount that was actually applied. | [optional] 
**type** | **str** | The type of the tax rate. Default is &#x60;PERCENT&#x60;.  The value &#x60;EXTERNAL&#x60; indicates that the tax is for a marketplace facilitator order, and that the marketplace facilitator organization calculated the tax amount.  | [optional] 
**facilitator_collect_and_remit_tax** | **bool** | Indicates whether the marketplace facilitator that received a guest order remitted the tax amount on behalf of the Toast platform restaurant.  You can use this information to identify tax amounts that have already been paid by an ordering service provider and do not need to be paid again.  * &#x60;true&#x60; - The marketplace facilitator paid the tax amount on behalf of the Toast platform restaurant location.  * &#x60;false&#x60; - The marketplace facilitator has not paid the tax amount. The Toast platform restaurant location may be required to pay the tax amount.  **Note**: Toast API response data is not guidance or advice for tax compliance.  | [optional] 
**display_name** | **str** | The name of the tax rate as it appears on guest receipts. | [optional] 
**jurisdiction** | **str** | The state or province of the tax rate for reporting purposes. | [optional] 
**jurisdiction_type** | **str** | The jurisdiction type (ex. STATE, COUNTY, etc.) of the tax rate for reporting purposes. | [optional] 

## Example

```python
from toastapi.models.applied_tax_rate import AppliedTaxRate

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedTaxRate from a JSON string
applied_tax_rate_instance = AppliedTaxRate.from_json(json)
# print the JSON string representation of the object
print(AppliedTaxRate.to_json())

# convert the object into a dict
applied_tax_rate_dict = applied_tax_rate_instance.to_dict()
# create an instance of AppliedTaxRate from a dict
applied_tax_rate_from_dict = AppliedTaxRate.from_dict(applied_tax_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


