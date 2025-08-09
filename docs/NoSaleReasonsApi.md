# toastapi.NoSaleReasonsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**no_sale_reasons_get**](NoSaleReasonsApi.md#no_sale_reasons_get) | **GET** /config/v2/noSaleReasons | Get no sale reasons
[**no_sale_reasons_guid_get**](NoSaleReasonsApi.md#no_sale_reasons_guid_get) | **GET** /config/v2/noSaleReasons/{guid} | Get a no sale reason


# **no_sale_reasons_get**
> List[NoSaleReason] no_sale_reasons_get(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)

Get no sale reasons

Returns an array of `NoSaleReason` objects containing information about no sale reasons configured for a restaurant.

### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.no_sale_reason import NoSaleReason
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
    api_instance = toastapi.NoSaleReasonsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to.
    page_token = 'page_token_example' # str | A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the `pageToken` parameter from the `Toast-Next-Page-Token` header field value of a previous request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html. (optional)
    last_modified = '2024-06-20T00:00:00.000+0000' # str | Limits the return data to objects created or modified after a specific date and time. For example: `2024-06-20T00:00:00.000+0000`. (optional)

    try:
        # Get no sale reasons
        api_response = await api_instance.no_sale_reasons_get(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)
        print("The response of NoSaleReasonsApi->no_sale_reasons_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NoSaleReasonsApi->no_sale_reasons_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to. | 
 **page_token** | **str**| A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the &#x60;pageToken&#x60; parameter from the &#x60;Toast-Next-Page-Token&#x60; header field value of a previous request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html. | [optional] 
 **last_modified** | **str**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2024-06-20T00:00:00.000+0000&#x60;. | [optional] 

### Return type

[**List[NoSaleReason]**](NoSaleReason.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of &#x60;NoSaleReason&#x60; objects. |  * Toast-Next-Page-Token - A string that identifies the following set of objects that the endpoint will return. You can use this value to retrieve that page of response data. To return the next page of objects you supply this value in the \&quot;pageToken\&quot; parameter of the next request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **no_sale_reasons_guid_get**
> NoSaleReason no_sale_reasons_guid_get(toast_restaurant_external_id, guid)

Get a no sale reason

Returns a `NoSaleReason` object containing information about a no sale reason.

### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.no_sale_reason import NoSaleReason
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
    api_instance = toastapi.NoSaleReasonsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to.
    guid = 'guid_example' # str | The Toast POS GUID of the no sale reason.

    try:
        # Get a no sale reason
        api_response = await api_instance.no_sale_reasons_guid_get(toast_restaurant_external_id, guid)
        print("The response of NoSaleReasonsApi->no_sale_reasons_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NoSaleReasonsApi->no_sale_reasons_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to. | 
 **guid** | **str**| The Toast POS GUID of the no sale reason. | 

### Return type

[**NoSaleReason**](NoSaleReason.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a &#x60;NoSaleReason&#x60; object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

