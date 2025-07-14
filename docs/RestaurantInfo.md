# RestaurantInfo

Information about the configuration of a restaurant in the Toast POS. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional] 
**general** | [**General**](General.md) |  | [optional] 
**urls** | [**URLs**](URLs.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**schedules** | [**Schedules**](Schedules.md) |  | [optional] 
**delivery** | [**Delivery**](Delivery.md) |  | [optional] 
**online_ordering** | [**OnlineOrdering**](OnlineOrdering.md) |  | [optional] 
**prep_times** | [**PrepTimes**](PrepTimes.md) |  | [optional] 

## Example

```python
from toastapi.models.restaurant_info import RestaurantInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantInfo from a JSON string
restaurant_info_instance = RestaurantInfo.from_json(json)
# print the JSON string representation of the object
print(RestaurantInfo.to_json())

# convert the object into a dict
restaurant_info_dict = restaurant_info_instance.to_dict()
# create an instance of RestaurantInfo from a dict
restaurant_info_from_dict = RestaurantInfo.from_dict(restaurant_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


