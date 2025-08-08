# toastapi.MenusV2Api

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**menus_v2_get**](MenusV2Api.md#menus_v2_get) | **GET** /menus/v2/menus | Get menus (V2)
[**menus_v2_metadata_get**](MenusV2Api.md#menus_v2_metadata_get) | **GET** /menus/v2/metadata | Get menu last modified timestamp (V2)


# **menus_v2_get**
> Restaurant menus_v2_get(toast_restaurant_external_id)

Get menus (V2)

Get menus

_Important:_ Ordering integrations should use menus API V3. Other integration types should continue to use menus API V2 until further notice. See <a href="https://doc.toasttab.com/doc/devguide/apiComparingMenusAPIV2AndV3.html">Comparing menus API V2 and V3</a> for more information.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.restaurant import Restaurant
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
    api_instance = toastapi.MenusV2Api(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier for the restaurant.

    try:
        # Get menus (V2)
        api_response = await api_instance.menus_v2_get(toast_restaurant_external_id)
        print("The response of MenusV2Api->menus_v2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusV2Api->menus_v2_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier for the restaurant. | 

### Return type

[**Restaurant**](Restaurant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | No published data was found for the restaurant. Ensure that the restaurant GUID is correct and that its data has been published. |  -  |
**503** | Unable to retrieve menus for the restaurant due to a service outage. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menus_v2_metadata_get**
> Metadata menus_v2_metadata_get(toast_restaurant_external_id)

Get menu last modified timestamp (V2)

A lightweight endpoint that allows you to determine if a restaurant's menu data has been updated. Toast support strongly recommends that you do not make a call to the `/menus` endpoint unless the date and time returned by the `/metadata` endpoint is more recent than the `lastUpdated` date and time. While this recommendation applies to all clients of the menus API, it is particularly important for clients that have limited bandwidth.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.metadata import Metadata
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
    api_instance = toastapi.MenusV2Api(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier for the restaurant.

    try:
        # Get menu last modified timestamp (V2)
        api_response = await api_instance.menus_v2_metadata_get(toast_restaurant_external_id)
        print("The response of MenusV2Api->menus_v2_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusV2Api->menus_v2_metadata_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier for the restaurant. | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

