# Order

A Toast platform order is composed of one or more checks. Each check has  one or more menu item selections. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**opened_date** | **datetime** | The business date of the order.  | [optional] 
**modified_date** | **datetime** | The most recent date that the order, or a check or menu item selection in the order, was modified. | [optional] 
**promised_date** | **datetime** | For scheduled orders, the date and time that the order is scheduled to be fulfilled.  | [optional] 
**dining_option** | **object** |  | 
**checks** | [**List[Check]**](Check.md) | The checks for this order. Most orders have one check.  | 
**delivery_info** | **object** |  | [optional] 
**number_of_guests** | **int** | The number of restaurant guests that are associated with the order.  | [optional] 
**voided** | **bool** | Set to &#x60;true&#x60; if this order was voided. Response only. | [optional] 
**void_date** | **datetime** | The date on which this order was voided. Response only. | [optional] 
**paid_date** | **datetime** | The most recent date on which this order received payment. | [optional] 
**business_date** | **int** | The business date (yyyyMMdd) on which the order was fulfilled. Response only. | [optional] 
**server** | **object** |  | [optional] 
**created_date** | **datetime** | The date and time that the Toast platform received the order. | [optional] 

## Example

```python
from toastapi.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


