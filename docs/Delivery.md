# Delivery

Information about the delivery configuration for the restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether the restaurant has enabled the Toast delivery module. This value is &#x60;true&#x60; if the module has ever been enabled. The value _does not_ indicate that a restaurant is accepting delivery orders or that the restaurant is using the Toast delivery feature.  | [optional] 
**radius** | **float** | The radius, in miles, of the delivery area for the restaurant.  | [optional] 
**coordinates** | **str** | The delivery area coordinates for the restaurant, encoded as a polyline using the Google polyline algorithm (https://github.com/mapbox/polyline). The delivery area coordinates are a JSON array of decimal degree latitude and longitude pairs. For example, &#x60;[[42.36083,-71.14798],[42.34028,-71.15673],[42.3272,-71.14386]]&#x60;.  | [optional] 

## Example

```python
from toastapi.models.delivery import Delivery

# TODO update the JSON string below
json = "{}"
# create an instance of Delivery from a JSON string
delivery_instance = Delivery.from_json(json)
# print the JSON string representation of the object
print(Delivery.to_json())

# convert the object into a dict
delivery_dict = delivery_instance.to_dict()
# create an instance of Delivery from a dict
delivery_from_dict = Delivery.from_dict(delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


