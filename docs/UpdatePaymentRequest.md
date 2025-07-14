# UpdatePaymentRequest

A wrapper object containing payment fields that you can update. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tip_amount** | **float** | The amount tipped on a payment.  | [optional] 

## Example

```python
from toastapi.models.update_payment_request import UpdatePaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentRequest from a JSON string
update_payment_request_instance = UpdatePaymentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePaymentRequest.to_json())

# convert the object into a dict
update_payment_request_dict = update_payment_request_instance.to_dict()
# create an instance of UpdatePaymentRequest from a dict
update_payment_request_from_dict = UpdatePaymentRequest.from_dict(update_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


