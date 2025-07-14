# AlternatePaymentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**name** | **str** | The name of the alternate payment type. | [optional] 

## Example

```python
from toastapi.models.alternate_payment_type import AlternatePaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of AlternatePaymentType from a JSON string
alternate_payment_type_instance = AlternatePaymentType.from_json(json)
# print the JSON string representation of the object
print(AlternatePaymentType.to_json())

# convert the object into a dict
alternate_payment_type_dict = alternate_payment_type_instance.to_dict()
# create an instance of AlternatePaymentType from a dict
alternate_payment_type_from_dict = AlternatePaymentType.from_dict(alternate_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


