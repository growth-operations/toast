# GuestReportingDataInProgress

Response when the Toast platform is still processing the reporting data request. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A brief message describing that the reporting data is still in progress and to try again at a later time.  | [optional] 
**report_request_guid** | **str** | The Toast platform assigned identifier used to identify a specific analytics reporting data request.  | [optional] 
**report_status** | **str** | Reflects the in progress status of the reporting data using the IN_PROGRESS value.  | [optional] 

## Example

```python
from toastapi.models.guest_reporting_data_in_progress import GuestReportingDataInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of GuestReportingDataInProgress from a JSON string
guest_reporting_data_in_progress_instance = GuestReportingDataInProgress.from_json(json)
# print the JSON string representation of the object
print(GuestReportingDataInProgress.to_json())

# convert the object into a dict
guest_reporting_data_in_progress_dict = guest_reporting_data_in_progress_instance.to_dict()
# create an instance of GuestReportingDataInProgress from a dict
guest_reporting_data_in_progress_from_dict = GuestReportingDataInProgress.from_dict(guest_reporting_data_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


