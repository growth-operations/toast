# Payment

Defines a payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**paid_date** | **datetime** | The date on which the payment was made. | [optional] 
**type** | **str** | The payment method.  | 
**amount** | **float** | The amount of this payment, excluding tips. | 
**tip_amount** | **float** | The amount tipped on this payment. | 
**amount_tendered** | **float** | The amount tendered for this payment. | [optional] 
**card_type** | **str** | The type of credit card that was used. Response only. | [optional] 
**last4_digits** | **str** | The last 4 digits of the credit card that was used. Response only. | [optional] 
**server** | **object** |  | [optional] 
**refund_status** | **str** | Indicates whether the payment was refunded. Response only.  | [optional] 
**payment_status** | **str** | The status of this payment when the type is &#x60;CREDIT&#x60;. Response only.  | [optional] 
**other_payment** | [**ExternalReference**](ExternalReference.md) |  | [optional] 

## Example

```python
from toastapi.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


