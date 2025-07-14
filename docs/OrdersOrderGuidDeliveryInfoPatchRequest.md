# OrdersOrderGuidDeliveryInfoPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivered_date** | **datetime** | The date on which the order was delivered.  | [optional] 
**dispatched_date** | **datetime** | The date on which the order was dispatched. If &#x60;dispatchedDate&#x60; is not specified, it is set to the current system time.  | [optional] 
**delivery_state** | **str** | The delivery state of the order.  | [optional] 
**delivery_employee** | **str** | The Toast platform identifier of the employee who is delivering the order.  | [optional] 

## Example

```python
from toastapi.models.orders_order_guid_delivery_info_patch_request import OrdersOrderGuidDeliveryInfoPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersOrderGuidDeliveryInfoPatchRequest from a JSON string
orders_order_guid_delivery_info_patch_request_instance = OrdersOrderGuidDeliveryInfoPatchRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersOrderGuidDeliveryInfoPatchRequest.to_json())

# convert the object into a dict
orders_order_guid_delivery_info_patch_request_dict = orders_order_guid_delivery_info_patch_request_instance.to_dict()
# create an instance of OrdersOrderGuidDeliveryInfoPatchRequest from a dict
orders_order_guid_delivery_info_patch_request_from_dict = OrdersOrderGuidDeliveryInfoPatchRequest.from_dict(orders_order_guid_delivery_info_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


