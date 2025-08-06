# MarketplaceFacilitatorTaxInfo

Information about the taxes that a marketplace facilitator organization remits on behalf of a Toast platform restaurant. `POST` only. The orders API does not include the `MarketplaceFacilitatorTaxInfo` object in response data.  **Note**: you can only include this information if your Toast API client is associated with a designated marketplace facilitator organization. Most Toast API clients do not create marketplace facilitator orders. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facilitator_collect_and_remit_tax_order** | **bool** | Indicates whether a marketplace facilitator organization has paid the tax amounts for an order on behalf of the restaurant that fulfills the order.  If you include this value, you indicate that the marketplace facilitator order uses the prices and tax amounts calculated by the Toast platform.  If you include this value, you *must not* include the &#x60;taxes&#x60; value and you *must not* include the &#x60;externalPriceAmount&#x60; for menu item selections in the order.  | [optional] 
**taxes** | [**List[AppliedTaxRate]**](AppliedTaxRate.md) | An array of &#x60;AppliedTaxRate&#x60; objects that describe the tax amounts that apply to a marketplace facilitator order.  If you include this value, you must include an &#x60;externalPriceAmount&#x60; for each menu item selection in the order.  | [optional] 

## Example

```python
from toastapi.models.marketplace_facilitator_tax_info import MarketplaceFacilitatorTaxInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceFacilitatorTaxInfo from a JSON string
marketplace_facilitator_tax_info_instance = MarketplaceFacilitatorTaxInfo.from_json(json)
# print the JSON string representation of the object
print(MarketplaceFacilitatorTaxInfo.to_json())

# convert the object into a dict
marketplace_facilitator_tax_info_dict = marketplace_facilitator_tax_info_instance.to_dict()
# create an instance of MarketplaceFacilitatorTaxInfo from a dict
marketplace_facilitator_tax_info_from_dict = MarketplaceFacilitatorTaxInfo.from_dict(marketplace_facilitator_tax_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


