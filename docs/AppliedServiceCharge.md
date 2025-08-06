# AppliedServiceCharge

A service charge that is added to a check. A service charge can represent an upcharge such as a gratuity or a delivery fee.  Whether the upcharge is taxable is defined in the restaurant-configured `serviceCharge`.  The fields on the `AppliedServiceCharge` are calculated based on the referenced `ServiceCharge` configuration. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**charge_amount** | **float** | The final applied amount excluding tax. Required if &#x60;chargeType&#x60; is &#x60;OPEN&#x60;. | [optional] 
**service_charge** | [**ExternalReference**](ExternalReference.md) |  | 
**charge_type** | **str** | The type of service charge. Response only.  Valid values:  * &#x60;FIXED&#x60; - The service charge is for a specific currency amount.  * &#x60;PERCENT&#x60; - The service charge is for a percentage of the check amount.  * &#x60;OPEN&#x60; - The service charge is not configured with an amount. The amount is specified by the restaurant employee.  | [optional] 
**name** | **str** | The configured human readable label for the service charge. Response only. | [optional] 
**delivery** | **bool** | Whether this service charge is a delivery charge. Response only. | [optional] 
**takeout** | **bool** | Whether this service charge is a takeout charge. Response only. | [optional] 
**dine_in** | **bool** | Whether this service charge is a dine-in charge. Response only. | [optional] 
**gratuity** | **bool** | Whether this service charge is a gratuity. Can be used to derive required tip amount on the check. Response only. | [optional] 
**taxable** | **bool** | Whether this service charge is taxable. Response only. | [optional] 
**applied_taxes** | [**List[AppliedTaxRate]**](AppliedTaxRate.md) | Taxes applied to the service charge. | [optional] 
**service_charge_calculation** | **str** | Defines whether a &#x60;PERCENT&#x60; service charge is applied before (&#x60;PRE_DISCOUNT&#x60;) or after (&#x60;POST_DISCOUNT&#x60;) discounts.  This field is &#x60;null&#x60; for &#x60;FIXED&#x60; and &#x60;OPEN&#x60; service charges.  | [optional] 
**refund_details** | [**RefundDetails**](RefundDetails.md) |  | [optional] 
**service_charge_category** | **str** | The type of service charge. Default is &#x60;SERVICE_CHARGE&#x60;. Response only.  Valid values:  * &#x60;SERVICE_CHARGE&#x60; - The default type for a service charge.  * &#x60;CREDIT_CARD_SURCHARGE&#x60; - A fee assessed _only_ on payment transactions that use a credit card.  * &#x60;FUNDRAISING_CAMPAIGN&#x60; - Service charge associated with fundraising.  | [optional] 
**payment_guid** | **str** | The Toast platform unique identifier for the payment the fee is linked to. The &#x60;paymentGuid&#x60; value is always &#x60;null&#x60; unless the &#x60;serviceChargeCategory&#x60; object value is &#x60;CREDIT_CARD_SURCHARGE&#x60;. Response only. | [optional] 

## Example

```python
from toastapi.models.applied_service_charge import AppliedServiceCharge

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedServiceCharge from a JSON string
applied_service_charge_instance = AppliedServiceCharge.from_json(json)
# print the JSON string representation of the object
print(AppliedServiceCharge.to_json())

# convert the object into a dict
applied_service_charge_dict = applied_service_charge_instance.to_dict()
# create an instance of AppliedServiceCharge from a dict
applied_service_charge_from_dict = AppliedServiceCharge.from_dict(applied_service_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


