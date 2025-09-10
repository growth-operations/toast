# DeliveryInfo

Information related to delivery orders. Required if the dining option behavior is `DELIVERY`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | The first line of the street address of the delivery destination.  | [optional] 
**address2** | **str** | The second line of the street address of the delivery destination.  | [optional] 
**city** | **str** | The name of the city or town of the delivery destination.  | [optional] 
**state** | **str** | The postal abbreviation of the state or province of the delivery destination.  | [optional] 
**zip_code** | **str** | The postal or zip code of the delivery destination.  | [optional] 
**administrative_area** | **str** | The state, province, or other geographic division that is larger than a city or town of the delivery destination.  | [optional] 
**country** | **str** | The two-character ISO-3166-2 country code of the delivery destination.  | [optional] 
**latitude** | **float** | The north/south geographic coordinate of the delivery destination, in decimal format.  | [optional] 
**longitude** | **float** | The east/west geographic coordinate of the delivery destination, in decimal format.  | [optional] 
**notes** | **str** | Additional instructions or information about the delivery.  | [optional] 
**delivered_date** | **datetime** | The date and time that the delivery employee indicated in the Toast POS app that the order was delivered. Response only.  | [optional] 
**dispatched_date** | **datetime** | The date and time that the restaurant indicated in the Toast POS app that the order was available for delivery and assigned to a delivery employee.  | [optional] 
**delivery_employee** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**delivery_state** | **str** | An internal representation of the state of a delivery order.  | [optional] 

## Example

```python
from toastapi.models.delivery_info import DeliveryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryInfo from a JSON string
delivery_info_instance = DeliveryInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveryInfo.to_json())

# convert the object into a dict
delivery_info_dict = delivery_info_instance.to_dict()
# create an instance of DeliveryInfo from a dict
delivery_info_from_dict = DeliveryInfo.from_dict(delivery_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


