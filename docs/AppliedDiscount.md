# AppliedDiscount

A discount applied to a check or item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**name** | **str** | The name of the applied discount. | [optional] 
**discount_amount** | **float** | The discount amount. This amount is subtracted from the check or item. | [optional] 
**discount** | **object** |  | [optional] 
**approver** | **object** |  | [optional] 
**discount_type** | **str** | The behavior of this discount.  | [optional] 
**discount_percent** | **float** | The percent value (0-100) of the applied discount when the &#x60;discountType&#x60; is &#x60;PERCENT&#x60; or &#x60;OPEN_PERCENT&#x60;. | [optional] 

## Example

```python
from toastapi.models.applied_discount import AppliedDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedDiscount from a JSON string
applied_discount_instance = AppliedDiscount.from_json(json)
# print the JSON string representation of the object
print(AppliedDiscount.to_json())

# convert the object into a dict
applied_discount_dict = applied_discount_instance.to_dict()
# create an instance of AppliedDiscount from a dict
applied_discount_from_dict = AppliedDiscount.from_dict(applied_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


