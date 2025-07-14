# TimeSpecificPriceV2

Represents the pricing rules for a menu item that uses a time-specific price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_specific_price** | **float** | The price during the periods defined by the schedule. | [optional] 
**base_price** | **float** | The base price used for time periods when a time-specific price has not been defined. | [optional] 
**schedule** | [**List[ScheduleV2]**](ScheduleV2.md) | An array of Schedule objects. | [optional] 

## Example

```python
from toastapi.models.time_specific_price_v2 import TimeSpecificPriceV2

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpecificPriceV2 from a JSON string
time_specific_price_v2_instance = TimeSpecificPriceV2.from_json(json)
# print the JSON string representation of the object
print(TimeSpecificPriceV2.to_json())

# convert the object into a dict
time_specific_price_v2_dict = time_specific_price_v2_instance.to_dict()
# create an instance of TimeSpecificPriceV2 from a dict
time_specific_price_v2_from_dict = TimeSpecificPriceV2.from_dict(time_specific_price_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


