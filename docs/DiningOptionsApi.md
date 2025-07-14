# toastapi.DiningOptionsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dining_options_get**](DiningOptionsApi.md#dining_options_get) | **GET** /config/v2/diningOptions | Get dining options 
[**dining_options_guid_get**](DiningOptionsApi.md#dining_options_guid_get) | **GET** /config/v2/diningOptions/{guid} | Get a dining option 


# **dining_options_get**
> List[DiningOption] dining_options_get(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)

Get dining options 

Returns an array of `DiningOption` objects containing information about dining options configured for a restaurant.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.dining_option import DiningOption
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
    api_instance = toastapi.DiningOptionsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
    page_token = 'page_token_example' # str | A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the `pageToken` parameter from the `Toast-Next-Page-Token` header field value of a previous request to the endpoint. For more information, see <a href=\"https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\">Paginating response data</a>.  (optional)
    last_modified = '2013-10-20T19:20:30+01:00' # datetime | Limits the return data to objects created or modified after a specific date and time. For example: `2024-06-20T00:00:00.000%2B0000`.  (optional)

    try:
        # Get dining options 
        api_response = await api_instance.dining_options_get(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)
        print("The response of DiningOptionsApi->dining_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiningOptionsApi->dining_options_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_token** | **str**| A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the &#x60;pageToken&#x60; parameter from the &#x60;Toast-Next-Page-Token&#x60; header field value of a previous request to the endpoint. For more information, see &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\&quot;&gt;Paginating response data&lt;/a&gt;.  | [optional] 
 **last_modified** | **datetime**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2024-06-20T00:00:00.000%2B0000&#x60;.  | [optional] 

### Return type

[**List[DiningOption]**](DiningOption.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of &#x60;DiningOption&#x60; objects. |  * Toast-Next-Page-Token - A string that identifies the following set of objects that the endpoint will return. You can use this value to retrieve that page of response data. To return the next page of objects you supply this value in the &#x60;pageToken&#x60; parameter of the next request to the endpoint. For more information, see &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\&quot;&gt;Paginating response data&lt;/a&gt;.  The endpoint does not return the &#x60;Toast-Next-Page-Token&#x60; field if there is no following page of response data objects. For example, the endpoint will not return a &#x60;Toast-Next-Page-Token&#x60; header field if all the data objects fit in one response or if you have reached the last page of response objects.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dining_options_guid_get**
> DiningOption dining_options_guid_get(toast_restaurant_external_id, guid)

Get a dining option 

Returns a `DiningOption` object containing information about a dining option configured for a restaurant.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.dining_option import DiningOption
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
    api_instance = toastapi.DiningOptionsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the dining option is configured for. 
    guid = 'guid_example' # str | The Toast POS GUID of the dining option.

    try:
        # Get a dining option 
        api_response = await api_instance.dining_options_guid_get(toast_restaurant_external_id, guid)
        print("The response of DiningOptionsApi->dining_options_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiningOptionsApi->dining_options_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the dining option is configured for.  | 
 **guid** | **str**| The Toast POS GUID of the dining option. | 

### Return type

[**DiningOption**](DiningOption.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a &#x60;DiningOption&#x60; object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

