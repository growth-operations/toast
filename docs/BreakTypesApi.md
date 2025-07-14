# toastapi.BreakTypesApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**break_types_get**](BreakTypesApi.md#break_types_get) | **GET** /config/v2/breakTypes | Get break types 
[**break_types_guid_get**](BreakTypesApi.md#break_types_guid_get) | **GET** /config/v2/breakTypes/{guid} | Get a break type 


# **break_types_get**
> List[BreakType] break_types_get(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)

Get break types 

Returns an array of `BreakType`
objects containing information about breaks configured for a
restaurant. If a `lastModified` date is specified, returns
all objects that were created or modified after that date.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.break_type import BreakType
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
    api_instance = toastapi.BreakTypesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
    page_token = 'page_token_example' # str | A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the `pageToken` parameter from the `Toast-Next-Page-Token` header field value of a previous request to the endpoint. For more information, see <a href=\"https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\">Paginating response data</a>.  (optional)
    last_modified = '2013-10-20T19:20:30+01:00' # datetime | Limits the return data to objects created or modified after a specific date and time. For example: `2024-06-20T00:00:00.000%2B0000`.  (optional)

    try:
        # Get break types 
        api_response = await api_instance.break_types_get(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)
        print("The response of BreakTypesApi->break_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakTypesApi->break_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_token** | **str**| A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the &#x60;pageToken&#x60; parameter from the &#x60;Toast-Next-Page-Token&#x60; header field value of a previous request to the endpoint. For more information, see &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\&quot;&gt;Paginating response data&lt;/a&gt;.  | [optional] 
 **last_modified** | **datetime**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2024-06-20T00:00:00.000%2B0000&#x60;.  | [optional] 

### Return type

[**List[BreakType]**](BreakType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of &#x60;BreakType&#x60; objects. |  * Toast-Next-Page-Token - A string that identifies the following set of objects that the endpoint will return. You can use this value to retrieve that page of response data. To return the next page of objects you supply this value in the &#x60;pageToken&#x60; parameter of the next request to the endpoint. For more information, see &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\&quot;&gt;Paginating response data&lt;/a&gt;.  The endpoint does not return the &#x60;Toast-Next-Page-Token&#x60; field if there is no following page of response data objects. For example, the endpoint will not return a &#x60;Toast-Next-Page-Token&#x60; header field if all the data objects fit in one response or if you have reached the last page of response objects.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **break_types_guid_get**
> BreakType break_types_guid_get(toast_restaurant_external_id, guid)

Get a break type 

Returns a `BreakType`
object containing information about a break type configured for 
a restaurant.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.break_type import BreakType
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
    api_instance = toastapi.BreakTypesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the break is configured for. 
    guid = 'guid_example' # str | The Toast POS GUID of the break config.

    try:
        # Get a break type 
        api_response = await api_instance.break_types_guid_get(toast_restaurant_external_id, guid)
        print("The response of BreakTypesApi->break_types_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakTypesApi->break_types_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the break is configured for.  | 
 **guid** | **str**| The Toast POS GUID of the break config. | 

### Return type

[**BreakType**](BreakType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a &#x60;BreakType&#x60; object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

