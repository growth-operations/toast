# Restaurant

Information about the restaurant whose menu data has been retrieved. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restaurant_guid** | **str** | A unique identifier for this restaurant, assigned by the Toast POS system.  | [optional] 
**last_updated** | **str** | The most recent date and time that this menu&#39;s data was published. Use this value to determine if you need to refresh your menu data. The &#x60;lastUpdated&#x60; value uses the absolute timestamp format describe in the &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/api_dates_and_timestamps.html\&quot;&gt;Dates and timestamps&lt;/a&gt; section of the Toast Developer Guide.  | [optional] 
**restaurant_time_zone** | **str** | The name of the restaurant&#39;s time zone in the IANA time zone database https://www.iana.org/time-zones. For example, \&quot;America/New_York\&quot;.  | [optional] 
**menus** | [**List[Menu]**](Menu.md) | An array of &#x60;Menu&#x60; objects that represent the published menus used by this restaurant.  | [optional] 
**modifier_group_references** | [**RestaurantModifierGroupReferences**](RestaurantModifierGroupReferences.md) |  | [optional] 
**modifier_option_references** | [**RestaurantModifierOptionReferences**](RestaurantModifierOptionReferences.md) |  | [optional] 
**pre_modifier_group_references** | [**RestaurantPreModifierGroupReferences**](RestaurantPreModifierGroupReferences.md) |  | [optional] 

## Example

```python
from toastapi.models.restaurant import Restaurant

# TODO update the JSON string below
json = "{}"
# create an instance of Restaurant from a JSON string
restaurant_instance = Restaurant.from_json(json)
# print the JSON string representation of the object
print(Restaurant.to_json())

# convert the object into a dict
restaurant_dict = restaurant_instance.to_dict()
# create an instance of Restaurant from a dict
restaurant_from_dict = Restaurant.from_dict(restaurant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


