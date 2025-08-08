# TimeSpecificPrice

Represents the pricing rules for a menu item that uses a time-specific price. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_specific_price** | **float** | The price of the menu item during the periods of time defined by the associated &#x60;schedule&#x60; array.  | [optional] 
**base_price** | **float** | The base price of the menu item, used for time periods when a time-specific price has not been defined.  | [optional] 
**schedule** | [**List[Schedule]**](Schedule.md) | An array of &#x60;Schedule&#x60; objects that indicate the specific days and times that a time-specific price is available.  | [optional] 

## Example

```python
from toastapi.models.time_specific_price import TimeSpecificPrice

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpecificPrice from a JSON string
time_specific_price_instance = TimeSpecificPrice.from_json(json)
# print the JSON string representation of the object
print(TimeSpecificPrice.to_json())

# convert the object into a dict
time_specific_price_dict = time_specific_price_instance.to_dict()
# create an instance of TimeSpecificPrice from a dict
time_specific_price_from_dict = TimeSpecificPrice.from_dict(time_specific_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


