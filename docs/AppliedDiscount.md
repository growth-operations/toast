# AppliedDiscount

A discount applied to a check or item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**name** | **str** | The name of the applied discount. | [optional] 
**discount_amount** | **float** | The discount amount. This amount is subtracted from the check or item. | [optional] 
**discount** | [**ToastReference**](ToastReference.md) |  | [optional] 
**approver** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**discount_type** | **str** | The behavior of this discount.  | [optional] 
**discount_percent** | **float** | The percent value (0-100) of the applied discount when the &#x60;discountType&#x60; is &#x60;PERCENT&#x60; or &#x60;OPEN_PERCENT&#x60;. | [optional] 
**non_tax_discount_amount** | **float** | The discount amount, excluding the tax discount amount. Response only. | [optional] 
**triggers** | [**List[AppliedDiscountTrigger]**](AppliedDiscountTrigger.md) | The menu item selections in the check that triggered this discount to be applied. Response only. | [optional] 
**processing_state** | **str** | The validation state of a loyalty program discount. Response only.  Valid values:  * &#x60;PENDING_APPLIED&#x60; - The loyalty program discount is applied to the check but the loyalty program service provider has not validated it. The discount will appear on guest receipts.  * &#x60;APPLIED&#x60; - The loyalty program discount has been validated by the loyalty program service provider and will appear on guest receipts.  * &#x60;PENDING_VOID&#x60; - The loyalty program service provider rejected the discount. The discount is pending removal from the check.  * &#x60;VOID&#x60; - The loyalty program discount has been removed from the check because the loyalty program service provider rejected it.  | [optional] 
**applied_discount_reason** | [**AppliedDiscountReason**](AppliedDiscountReason.md) |  | [optional] 
**loyalty_details** | [**LoyaltyDetails**](LoyaltyDetails.md) |  | [optional] 
**combo_items** | [**List[ExternalReference]**](ExternalReference.md) | The menu item selections that are discounted as part of a combo discount. Response only. | [optional] 
**applied_promo_code** | **str** | The promo code that was applied to get this discount. Response only. | [optional] 

## Example

```python
from toastapi.models.applied_discount import AppliedDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedDiscount from a JSON string
applied_discount_instance = AppliedDiscount.from_json(json)
# print the JSON string representation of the object
print(AppliedDiscount.to_json())

# convert the object into a dict
applied_discount_dict = applied_discount_instance.to_dict()
# create an instance of AppliedDiscount from a dict
applied_discount_from_dict = AppliedDiscount.from_dict(applied_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


