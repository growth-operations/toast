# RestaurantService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**name** | **str** | The name of this meal service (for example, &#x60;Lunch&#x60; or &#x60;Dinner&#x60;).  | [optional] 

## Example

```python
from toastapi.models.restaurant_service import RestaurantService

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantService from a JSON string
restaurant_service_instance = RestaurantService.from_json(json)
# print the JSON string representation of the object
print(RestaurantService.to_json())

# convert the object into a dict
restaurant_service_dict = restaurant_service_instance.to_dict()
# create an instance of RestaurantService from a dict
restaurant_service_from_dict = RestaurantService.from_dict(restaurant_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


