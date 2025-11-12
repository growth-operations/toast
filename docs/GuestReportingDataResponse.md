# GuestReportingDataResponse

The guest reporting data organized by payment. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_fingerprint** | **str** | The identifier assigned by the Toast platform used to identify a guest&#39;s payment card.  | [optional] 
**order_guid** | **str** | The identifier assigned by the Toast platform used to identify an order.  | [optional] 
**payment_date** | **str** | The date when the payment was processed.  | [optional] 
**payment_guid** | **str** | The identifier assigned by the Toast platform used to identify the payment.  | [optional] 
**restaurant_guid** | **str** | The identifier assigned by the Toast platform used to identify a restaurant location.  | [optional] 
**restaurant_location_code** | **str** | The restaurant&#39;s location code.  | [optional] 
**restaurant_location_name** | **str** | The restaurant&#39;s location name.  | [optional] 
**restaurant_name** | **str** | The restaurant&#39;s name.  | [optional] 

## Example

```python
from toastapi.models.guest_reporting_data_response import GuestReportingDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuestReportingDataResponse from a JSON string
guest_reporting_data_response_instance = GuestReportingDataResponse.from_json(json)
# print the JSON string representation of the object
print(GuestReportingDataResponse.to_json())

# convert the object into a dict
guest_reporting_data_response_dict = guest_reporting_data_response_instance.to_dict()
# create an instance of GuestReportingDataResponse from a dict
guest_reporting_data_response_from_dict = GuestReportingDataResponse.from_dict(guest_reporting_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


