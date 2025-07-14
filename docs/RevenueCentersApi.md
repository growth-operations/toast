# toastapi.RevenueCentersApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revenue_centers_get**](RevenueCentersApi.md#revenue_centers_get) | **GET** /config/v2/revenueCenters | Get revenue centers
[**revenue_centers_guid_get**](RevenueCentersApi.md#revenue_centers_guid_get) | **GET** /config/v2/revenueCenters/{guid} | Get revenue center by GUID


# **revenue_centers_get**
> List[RevenueCenter] revenue_centers_get(toast_restaurant_external_id, limit=limit, page_token=page_token, last_modified=last_modified)

Get revenue centers

Returns an array of revenue centers for the restaurant.

### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.revenue_center import RevenueCenter
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
    api_instance = toastapi.RevenueCentersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier for the restaurant.
    limit = 300 # int | The maximum number of objects to return. The default value is 300. The maximum value is 300. (optional) (default to 300)
    page_token = 'page_token_example' # str | A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the \"pageToken\" parameter from the \"Toast-Next-Page-Token\" header field value of a previous request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html. (optional)
    last_modified = '2013-10-20T19:20:30+01:00' # datetime | Limits the return data to objects created or modified after a specific date and time. For example: '2024-06-20T00:00:00.000%2B0000'. (optional)

    try:
        # Get revenue centers
        api_response = await api_instance.revenue_centers_get(toast_restaurant_external_id, limit=limit, page_token=page_token, last_modified=last_modified)
        print("The response of RevenueCentersApi->revenue_centers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RevenueCentersApi->revenue_centers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier for the restaurant. | 
 **limit** | **int**| The maximum number of objects to return. The default value is 300. The maximum value is 300. | [optional] [default to 300]
 **page_token** | **str**| A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the \&quot;pageToken\&quot; parameter from the \&quot;Toast-Next-Page-Token\&quot; header field value of a previous request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html. | [optional] 
 **last_modified** | **datetime**| Limits the return data to objects created or modified after a specific date and time. For example: &#39;2024-06-20T00:00:00.000%2B0000&#39;. | [optional] 

### Return type

[**List[RevenueCenter]**](RevenueCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of &#x60;RevenueCenter&#x60; objects. |  * Toast-Next-Page-Token - A string that identifies the following set of objects that the endpoint will return. You can use this value to retrieve that page of response data. To return the next page of objects you supply this value in the \&quot;pageToken\&quot; parameter of the next request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revenue_centers_guid_get**
> RevenueCenter revenue_centers_guid_get(toast_restaurant_external_id, guid)

Get revenue center by GUID

Returns a specific revenue center by its GUID.

### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.revenue_center import RevenueCenter
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
    api_instance = toastapi.RevenueCentersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier for the restaurant.
    guid = 'guid_example' # str | The GUID of the revenue center.

    try:
        # Get revenue center by GUID
        api_response = await api_instance.revenue_centers_guid_get(toast_restaurant_external_id, guid)
        print("The response of RevenueCentersApi->revenue_centers_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RevenueCentersApi->revenue_centers_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier for the restaurant. | 
 **guid** | **str**| The GUID of the revenue center. | 

### Return type

[**RevenueCenter**](RevenueCenter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a &#x60;RevenueCenter&#x60; object. |  -  |
**404** | Revenue center not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

