# GuestReportingDataRequest

A JSON object containing the starting and ending dates for the reporting data request and included or excluded restaurants. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **int** | The starting date of the time range for the reporting data.  Specify the date in the format YYYYMMDD. For example, 20220824.  | 
**end_date** | **int** | The ending date of the time range for the reporting data.  Specify the date in the format YYYYMMDD. For example, 20220824.  | 
**restaurant_ids** | **List[str]** | The restaurantGuid values of specific restaurants in the management group to include in the reporting data. If used, only the data for listed restaurants in the management group that are identified by restaurantGuid is included. If left blank, all restaurants are included by default.  | 
**excluded_restaurant_ids** | **List[str]** | The restaurantGuid values of specific restaurants in the management group to exclude from the reporting data. If used, the data for listed restaurants in the management group that are identified by restaurantGuid is excluded. If left blank, all restaurants are included by default.  | 

## Example

```python
from toastapi.models.guest_reporting_data_request import GuestReportingDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GuestReportingDataRequest from a JSON string
guest_reporting_data_request_instance = GuestReportingDataRequest.from_json(json)
# print the JSON string representation of the object
print(GuestReportingDataRequest.to_json())

# convert the object into a dict
guest_reporting_data_request_dict = guest_reporting_data_request_instance.to_dict()
# create an instance of GuestReportingDataRequest from a dict
guest_reporting_data_request_from_dict = GuestReportingDataRequest.from_dict(guest_reporting_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


