# Check

Represents a single check within an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**created_date** | **datetime** | The date and time that the Toast platform received the check. | [optional] 
**opened_date** | **datetime** | The date on which this check was opened. If not specified, it is set to the current system time. | [optional] 
**closed_date** | **datetime** | The most recent date on which this check&#39;s payment status was set to &#x60;CLOSED&#x60;. | [optional] 
**modified_date** | **datetime** | The most recent date on which this check was modified. | [optional] 
**deleted_date** | **datetime** | The date on which this check was deleted.  &#x60;deletedDate&#x60; is only applicable when &#x60;deleted&#x60; is true.  If &#x60;deleted&#x60; is false, then &#x60;deletedDate&#x60; is set to the UNIX epoch, &#x60;1970-01-01T00:00:00.000+0000&#x60;.  | [optional] 
**deleted** | **bool** | Set to &#x60;true&#x60; if this check was deleted. | [optional] 
**selections** | [**List[Selection]**](Selection.md) |  | 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**applied_loyalty_info** | [**AppliedLoyaltyInfo**](AppliedLoyaltyInfo.md) |  | [optional] 
**tax_exempt** | **bool** | Set to &#x60;true&#x60; if this check is tax exempt. | [optional] [default to False]
**display_number** | **str** | Generally starts at one each day and counts up. The Toast platform fills this in if it is not specified when the order is POSTed. Not guaranteed to be unique. | [optional] 
**applied_service_charges** | [**List[AppliedServiceCharge]**](AppliedServiceCharge.md) | Any restaurant-configured service charges that applied to this check. | [optional] 
**amount** | **float** | The total calculated price of the check including discounts and service charges. The &#x60;amount&#x60; does not include gratuity or taxes. Response only. | [optional] 
**tax_amount** | **float** | The calculated tax amount. Includes service charge and item level taxes. Response only. | [optional] 
**total_amount** | **float** | The total calculated price of this check including discounts and taxes. Not affected by refunds. | [optional] 
**payments** | [**List[Payment]**](Payment.md) | Payments made on this check. | [optional] 
**tab_name** | **str** | The name of the tab on this check. This displays on the KDS (Kitchen Display System) for pending orders.  The &#x60;tabName&#x60; value can contain up to 255 characters.  | [optional] 
**payment_status** | **str** | The payment status of this check.  Valid values:  * &#x60;OPEN&#x60; - There is an outstanding balance.  * &#x60;PAID&#x60; - A credit card payment was applied, but the tip has not been adjusted.  * &#x60;CLOSED&#x60;  - There is no remaining amount due on this check. For credit card payments, the payment has been adjusted to reflect the tip. Toast does not prevent a &#x60;CLOSED&#x60; check from transitioning back to &#x60;OPEN&#x60; or &#x60;PAID&#x60;.  Response only.  | [optional] 
**applied_discounts** | [**List[AppliedDiscount]**](AppliedDiscount.md) | The discounts applied to this check. In a &#x60;POST&#x60; request, only one &#x60;appliedDiscount&#x60; is allowed per check. | [optional] 
**voided** | **bool** | True if this check is voided. Response only. | [optional] 
**void_date** | **datetime** | The date when this check was voided. Response only. | [optional] 
**void_business_date** | **int** | The business date (yyyyMMdd) on which this check was voided. Response only. | [optional] 
**paid_date** | **datetime** | The most recent date when this check received payment. If not specified when &#x60;POST&#x60;ing, it is set to the current system time. | [optional] 
**created_device** | [**Device**](Device.md) |  | [optional] 
**last_modified_device** | [**Device**](Device.md) |  | [optional] 
**duration** | **int** | The number of seconds between creation and payment. Response only. | [optional] 
**opened_by** | [**ExternalReference**](ExternalReference.md) |  | [optional] 

## Example

```python
from toastapi.models.check import Check

# TODO update the JSON string below
json = "{}"
# create an instance of Check from a JSON string
check_instance = Check.from_json(json)
# print the JSON string representation of the object
print(Check.to_json())

# convert the object into a dict
check_dict = check_instance.to_dict()
# create an instance of Check from a dict
check_from_dict = Check.from_dict(check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


