# PayoutReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**name** | **str** | The short name of this payout reason. | [optional] 

## Example

```python
from toastapi.models.payout_reason import PayoutReason

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutReason from a JSON string
payout_reason_instance = PayoutReason.from_json(json)
# print the JSON string representation of the object
print(PayoutReason.to_json())

# convert the object into a dict
payout_reason_dict = payout_reason_instance.to_dict()
# create an instance of PayoutReason from a dict
payout_reason_from_dict = PayoutReason.from_dict(payout_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


