# AppliedDiscountTrigger

The Selection that triggered the application of this discount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**quantity** | **float** | The amount of the selection used to trigger the applied discount. | [optional] 

## Example

```python
from toastapi.models.applied_discount_trigger import AppliedDiscountTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedDiscountTrigger from a JSON string
applied_discount_trigger_instance = AppliedDiscountTrigger.from_json(json)
# print the JSON string representation of the object
print(AppliedDiscountTrigger.to_json())

# convert the object into a dict
applied_discount_trigger_dict = applied_discount_trigger_instance.to_dict()
# create an instance of AppliedDiscountTrigger from a dict
applied_discount_trigger_from_dict = AppliedDiscountTrigger.from_dict(applied_discount_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


