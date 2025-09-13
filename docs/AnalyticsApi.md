# toastapi.AnalyticsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_guest_reporting_data_request**](AnalyticsApi.md#create_guest_reporting_data_request) | **POST** /era/v1/guest/payments/{timeRange} | Post a guest reporting data request organized by payment for a specific time range
[**get_guest_reporting_data**](AnalyticsApi.md#get_guest_reporting_data) | **GET** /era/v1/guest/payments/{reportRequestGuid} | Get the guest reporting data organized by payment


# **create_guest_reporting_data_request**
> str create_guest_reporting_data_request(time_range, guest_reporting_data_request, only_inactive_restaurants=only_inactive_restaurants)

Post a guest reporting data request organized by payment for a specific time range

Creates a guest reporting data organized by payment request for a specific time range.

Specify the time range with the timeRange path parameter.

Specify whether to include data from inactive restaurants using the onlyInactiveRestaurants query parameter.

Specify the startDate and endDate for the guest data in the message body.

Include information about which restaurants to include or exclude with the restaurantIds and excludedRestaurantIds properties.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.guest_reporting_data_request import GuestReportingDataRequest
from toastapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ws-sandbox-api.eng.toasttab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = toastapi.Configuration(
    host = "https://ws-sandbox-api.eng.toasttab.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with toastapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = toastapi.AnalyticsApi(api_client)
    time_range = 'time_range_example' # str | The specific time range that you are requesting reporting data for.  Valid values:  day - The request covers a one day time range.  week - The request covers a time range of seven days or fewer. 
    guest_reporting_data_request = toastapi.GuestReportingDataRequest() # GuestReportingDataRequest | A JSON object containing the starting and ending dates for the reporting data request and included or excluded restaurants. 
    only_inactive_restaurants = True # bool | Specifies whether the data is for inactive restaurants only. Active restaurant data is returned by default.  Valid values:  true - The data retrieved is for inactive restaurants only.  false - The data retrieved is for active restaurants only.  (optional)

    try:
        # Post a guest reporting data request organized by payment for a specific time range
        api_response = await api_instance.create_guest_reporting_data_request(time_range, guest_reporting_data_request, only_inactive_restaurants=only_inactive_restaurants)
        print("The response of AnalyticsApi->create_guest_reporting_data_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->create_guest_reporting_data_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_range** | **str**| The specific time range that you are requesting reporting data for.  Valid values:  day - The request covers a one day time range.  week - The request covers a time range of seven days or fewer.  | 
 **guest_reporting_data_request** | [**GuestReportingDataRequest**](GuestReportingDataRequest.md)| A JSON object containing the starting and ending dates for the reporting data request and included or excluded restaurants.  | 
 **only_inactive_restaurants** | **bool**| Specifies whether the data is for inactive restaurants only. Active restaurant data is returned by default.  Valid values:  true - The data retrieved is for inactive restaurants only.  false - The data retrieved is for active restaurants only.  | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reportRequestGuid used to retrieve the reporting data. |  -  |
**400** | The request contains invalid information. |  -  |
**500** | An unexpected internal error occurred. The requestId attached to this error can be referenced by the Toast support team.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guest_reporting_data**
> List[GuestReportingDataResponse] get_guest_reporting_data(report_request_guid)

Get the guest reporting data organized by payment

Returns the guest data organized by payment for the reporting data request.

Specify the reportRequestGuid for the reporting data.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.guest_reporting_data_response import GuestReportingDataResponse
from toastapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ws-sandbox-api.eng.toasttab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = toastapi.Configuration(
    host = "https://ws-sandbox-api.eng.toasttab.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with toastapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = toastapi.AnalyticsApi(api_client)
    report_request_guid = 'report_request_guid_example' # str | The Toast platform identifier for the reporting data request. 

    try:
        # Get the guest reporting data organized by payment
        api_response = await api_instance.get_guest_reporting_data(report_request_guid)
        print("The response of AnalyticsApi->get_guest_reporting_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_guest_reporting_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_request_guid** | **str**| The Toast platform identifier for the reporting data request.  | 

### Return type

[**List[GuestReportingDataResponse]**](GuestReportingDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reporting data. |  -  |
**202** | The Toast platform is in the process of gathering the reporting data. Try the request again at a later time.  |  -  |
**404** | An unexpected error occurred. Refer to the message attached to this error for more information.  |  -  |
**409** | The Toast platform was unable to process the request. Request a new reportRequestGuid and try again.  |  -  |
**500** | An unexpected internal error occurred. The requestId attached to this error can be referenced by the Toast support team.  |  -  |
**504** | The Toast platform was unable to process the request because internal services took too long to process.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

