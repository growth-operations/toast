# Check

Represents a single check within an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**created_date** | **datetime** | The date and time that the Toast platform received the check. | [optional] 
**opened_date** | **datetime** | The date on which this check was opened. | [optional] 
**selections** | [**List[Selection]**](Selection.md) |  | 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**amount** | **float** | The total calculated price of the check including discounts and service charges. | [optional] 
**tax_amount** | **float** | The calculated tax amount. | [optional] 
**total_amount** | **float** | The total calculated price of this check including discounts and taxes. | [optional] 
**payments** | [**List[Payment]**](Payment.md) | Payments made on this check. | [optional] 
**applied_discounts** | [**List[AppliedDiscount]**](AppliedDiscount.md) | The discounts applied to this check. | [optional] 
**voided** | **bool** | True if this check is voided. Response only. | [optional] 
**void_date** | **datetime** | The date when this check was voided. Response only. | [optional] 
**paid_date** | **datetime** | The most recent date when this check received payment. | [optional] 

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


