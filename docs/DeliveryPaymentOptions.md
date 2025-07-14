# DeliveryPaymentOptions

Information about the forms of payment that the restaurant will accept for delivery orders. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash** | **bool** | Indicates whether the restaurant accepts cash payment for delivery orders that are placed online.  | [optional] 
**cc_same_day** | **bool** | Indicates whether the restaurant accepts online credit card payment for delivery orders that are delivered on the same day.  | [optional] 
**cc_future** | **bool** | Indicates whether the restaurant accepts online credit card payment for delivery orders that are to be delivered on a day after the guest places the order.  | [optional] 

## Example

```python
from toastapi.models.delivery_payment_options import DeliveryPaymentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryPaymentOptions from a JSON string
delivery_payment_options_instance = DeliveryPaymentOptions.from_json(json)
# print the JSON string representation of the object
print(DeliveryPaymentOptions.to_json())

# convert the object into a dict
delivery_payment_options_dict = delivery_payment_options_instance.to_dict()
# create an instance of DeliveryPaymentOptions from a dict
delivery_payment_options_from_dict = DeliveryPaymentOptions.from_dict(delivery_payment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


