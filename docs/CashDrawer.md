# CashDrawer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**printer** | [**ToastReference**](ToastReference.md) |  | [optional] 

## Example

```python
from toastapi.models.cash_drawer import CashDrawer

# TODO update the JSON string below
json = "{}"
# create an instance of CashDrawer from a JSON string
cash_drawer_instance = CashDrawer.from_json(json)
# print the JSON string representation of the object
print(CashDrawer.to_json())

# convert the object into a dict
cash_drawer_dict = cash_drawer_instance.to_dict()
# create an instance of CashDrawer from a dict
cash_drawer_from_dict = CashDrawer.from_dict(cash_drawer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


