# VoidOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selections** | [**VoidOrderRequestSelections**](VoidOrderRequestSelections.md) |  | [optional] 
**payments** | [**VoidOrderRequestSelections**](VoidOrderRequestSelections.md) |  | [optional] 

## Example

```python
from toastapi.models.void_order_request import VoidOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoidOrderRequest from a JSON string
void_order_request_instance = VoidOrderRequest.from_json(json)
# print the JSON string representation of the object
print(VoidOrderRequest.to_json())

# convert the object into a dict
void_order_request_dict = void_order_request_instance.to_dict()
# create an instance of VoidOrderRequest from a dict
void_order_request_from_dict = VoidOrderRequest.from_dict(void_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


