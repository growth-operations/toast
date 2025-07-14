# RestaurantBasic

The Toast POS GUID for a restaurant 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The unique identifier that the Toast POS assigns to a restaurant.  | [optional] 

## Example

```python
from toastapi.models.restaurant_basic import RestaurantBasic

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantBasic from a JSON string
restaurant_basic_instance = RestaurantBasic.from_json(json)
# print the JSON string representation of the object
print(RestaurantBasic.to_json())

# convert the object into a dict
restaurant_basic_dict = restaurant_basic_instance.to_dict()
# create an instance of RestaurantBasic from a dict
restaurant_basic_from_dict = RestaurantBasic.from_dict(restaurant_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


