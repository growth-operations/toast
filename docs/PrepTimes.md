# PrepTimes

Information about the scheduled availability of the dining options that are provided by the restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_prep_time** | **int** | The amount of time, in minutes, that it takes to prepare an online delivery order.  | [optional] 
**delivery_time_after_open** | **int** | The amount of time, in minutes, that it takes for delivery service to become available after the restaurant opens.  | [optional] 
**delivery_time_before_close** | **int** | The amount of time, in minutes, before the restaurant closing time that delivery service becomes unavailable.  | [optional] 
**takeout_prep_time** | **int** | The amount of time, in minutes, that it takes to prepare an online takeout order.  | [optional] 
**takeout_time_after_open** | **int** | The amount of time, in minutes, that it takes for takeout service to become available after the restaurant opens.  | [optional] 
**takeout_time_before_close** | **int** | The amount of time, in minutes, before the restaurant closing time that takeout service becomes unavailable.  | [optional] 
**takeout_throttling_time** | **int** | The amount of time, in minutes, that an online takeout order is delayed before the Toast POS fires it in the kitchen.  | [optional] 
**delivery_throttling_time** | **int** | The amount of time, in minutes, that an online delivery order is delayed before the Toast POS fires it in the kitchen.  | [optional] 

## Example

```python
from toastapi.models.prep_times import PrepTimes

# TODO update the JSON string below
json = "{}"
# create an instance of PrepTimes from a JSON string
prep_times_instance = PrepTimes.from_json(json)
# print the JSON string representation of the object
print(PrepTimes.to_json())

# convert the object into a dict
prep_times_dict = prep_times_instance.to_dict()
# create an instance of PrepTimes from a dict
prep_times_from_dict = PrepTimes.from_dict(prep_times_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


