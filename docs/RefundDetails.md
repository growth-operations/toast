# RefundDetails

Information about refunded currency amounts for an item selection, modifier option, or service charge. The refund information includes separate values for the pre-tax value being refunded and the tax amount being refunded. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_amount** | **float** | The value of the menu item or service charge (excluding taxes) being refunded. Includes the value of any nested modifier options that increased the price of the item or modifier option (an upcharge for the modifier option).  | [optional] 
**tax_refund_amount** | **float** | The tax amount being refunded.  | [optional] 
**refund_transaction** | [**ToastReference**](ToastReference.md) |  | [optional] 

## Example

```python
from toastapi.models.refund_details import RefundDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RefundDetails from a JSON string
refund_details_instance = RefundDetails.from_json(json)
# print the JSON string representation of the object
print(RefundDetails.to_json())

# convert the object into a dict
refund_details_dict = refund_details_instance.to_dict()
# create an instance of RefundDetails from a dict
refund_details_from_dict = RefundDetails.from_dict(refund_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


