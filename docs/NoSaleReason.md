# NoSaleReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**name** | **str** | The name of the no sale reason that appears in the Toast POS. | [optional] 

## Example

```python
from toastapi.models.no_sale_reason import NoSaleReason

# TODO update the JSON string below
json = "{}"
# create an instance of NoSaleReason from a JSON string
no_sale_reason_instance = NoSaleReason.from_json(json)
# print the JSON string representation of the object
print(NoSaleReason.to_json())

# convert the object into a dict
no_sale_reason_dict = no_sale_reason_instance.to_dict()
# create an instance of NoSaleReason from a dict
no_sale_reason_from_dict = NoSaleReason.from_dict(no_sale_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


