# MenuV2Availability

An `Availability` object with information about the days and times this menu is available. If the menu is available 24 hours per day, 7 days per week, this `Availability` object contains a single value, `alwaysAvailable`, that is set to TRUE. If the menu is not available 24 hours per day, 7 days per week, the `alwaysAvailable` value is set to FALSE and the object will also contain a `schedule` value that provides detailed information about the specific days and times this menu is available.  **_Important_** The orders API does not validate against the availability settings of a menu, meaning it is possible to submit an order for an item on a menu when it is not currently available. For this reason, it is particularly important that you check a menu's `availability` value before placing an order from it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_available** | **bool** | Indicates whether this menu is available 24 hours per day, 7 days a week. If &#x60;alwaysAvailable&#x60; is FALSE, then a &#x60;schedule&#x60; value is included in the &#x60;Availability&#x60; object to define the specific times and days a menu is available. If &#x60;alwaysAvailable&#x60; is TRUE, then the &#x60;schedule&#x60; value is omitted.  | [optional] 
**schedule** | [**List[ScheduleV2]**](ScheduleV2.md) | An array of &#x60;Schedule&#x60; objects that indicate the specific days and times a menu is available. If &#x60;alwaysAvailable&#x60; is TRUE, then the menu is available 24 hours per day, 7 days per week, and this &#x60;schedule&#x60; value is omitted from the &#x60;Availabilty&#x60; object.  | [optional] 

## Example

```python
from toastapi.models.menu_v2_availability import MenuV2Availability

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV2Availability from a JSON string
menu_v2_availability_instance = MenuV2Availability.from_json(json)
# print the JSON string representation of the object
print(MenuV2Availability.to_json())

# convert the object into a dict
menu_v2_availability_dict = menu_v2_availability_instance.to_dict()
# create an instance of MenuV2Availability from a dict
menu_v2_availability_from_dict = MenuV2Availability.from_dict(menu_v2_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


