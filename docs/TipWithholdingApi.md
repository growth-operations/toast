# toastapi.TipWithholdingApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tip_withholding_get**](TipWithholdingApi.md#tip_withholding_get) | **GET** /config/v2/tipWithholding | Get tip withholding configuration


# **tip_withholding_get**
> TipWithholding tip_withholding_get(toast_restaurant_external_id)

Get tip withholding configuration

Returns the tip withholding configuration for the restaurant.

### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.tip_withholding import TipWithholding
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
    api_instance = toastapi.TipWithholdingApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier for the restaurant.

    try:
        # Get tip withholding configuration
        api_response = await api_instance.tip_withholding_get(toast_restaurant_external_id)
        print("The response of TipWithholdingApi->tip_withholding_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TipWithholdingApi->tip_withholding_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier for the restaurant. | 

### Return type

[**TipWithholding**](TipWithholding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a &#x60;TipWithholding&#x60; object. |  -  |
**404** | Tip withholding configuration not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

