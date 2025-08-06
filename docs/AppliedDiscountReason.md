# AppliedDiscountReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the reason for the applied discount. | 
**description** | **str** | An optional description for the reason for the applied discount. | [optional] 
**comment** | **str** | An optional comment on the reason for the applied discount. | [optional] 
**discount_reason** | [**ToastReference**](.md) |  | [optional] 

## Example

```python
from toastapi.models.applied_discount_reason import AppliedDiscountReason

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedDiscountReason from a JSON string
applied_discount_reason_instance = AppliedDiscountReason.from_json(json)
# print the JSON string representation of the object
print(AppliedDiscountReason.to_json())

# convert the object into a dict
applied_discount_reason_dict = applied_discount_reason_instance.to_dict()
# create an instance of AppliedDiscountReason from a dict
applied_discount_reason_from_dict = AppliedDiscountReason.from_dict(applied_discount_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


