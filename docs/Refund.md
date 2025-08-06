# Refund

A currency amount removed from a guest payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_amount** | **float** | The amount of the refund, excluding the tip. | [optional] 
**tip_refund_amount** | **float** | The amount of the tip refund. | [optional] 
**refund_date** | **datetime** | The date and time when the refund was made. | [optional] 
**refund_business_date** | **int** | The business date (yyyyMMdd) on which this refund was created. Response only. | [optional] 
**refund_transaction** | [**ToastReference**](.md) |  | [optional] 

## Example

```python
from toastapi.models.refund import Refund

# TODO update the JSON string below
json = "{}"
# create an instance of Refund from a JSON string
refund_instance = Refund.from_json(json)
# print the JSON string representation of the object
print(Refund.to_json())

# convert the object into a dict
refund_dict = refund_instance.to_dict()
# create an instance of Refund from a dict
refund_from_dict = Refund.from_dict(refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


