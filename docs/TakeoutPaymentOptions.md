# TakeoutPaymentOptions

Information about the forms of payment that the restaurant will accept for orders that a guest picks up in person. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash** | **bool** | Indicates whether the restaurant accepts cash payment for takeout orders that are placed online.  | [optional] 
**cc_same_day** | **bool** | Indicates whether the restaurant accepts online credit card payment for takeout orders that the guest will pick up on the same day.  | [optional] 
**cc_future** | **bool** | Indicates whether the restaurant accepts online credit card payment for takeout orders that the guest will pick up on a day after the guest places the order.  | [optional] 
**cc_in_store** | **bool** | Indicates whether the restaurant accepts credit card payment at the time the guest picks up a takeout order.  | [optional] 

## Example

```python
from toastapi.models.takeout_payment_options import TakeoutPaymentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TakeoutPaymentOptions from a JSON string
takeout_payment_options_instance = TakeoutPaymentOptions.from_json(json)
# print the JSON string representation of the object
print(TakeoutPaymentOptions.to_json())

# convert the object into a dict
takeout_payment_options_dict = takeout_payment_options_instance.to_dict()
# create an instance of TakeoutPaymentOptions from a dict
takeout_payment_options_from_dict = TakeoutPaymentOptions.from_dict(takeout_payment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


