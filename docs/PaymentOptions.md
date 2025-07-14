# PaymentOptions

Information about the forms of payment that the restaurant will accept for orders. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery** | [**DeliveryPaymentOptions**](DeliveryPaymentOptions.md) |  | [optional] 
**takeout** | [**TakeoutPaymentOptions**](TakeoutPaymentOptions.md) |  | [optional] 
**cc_tip** | **bool** | enables credit card tips | [optional] 

## Example

```python
from toastapi.models.payment_options import PaymentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOptions from a JSON string
payment_options_instance = PaymentOptions.from_json(json)
# print the JSON string representation of the object
print(PaymentOptions.to_json())

# convert the object into a dict
payment_options_dict = payment_options_instance.to_dict()
# create an instance of PaymentOptions from a dict
payment_options_from_dict = PaymentOptions.from_dict(payment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


