# toastapi.AuthenticationApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /authentication/v1/authentication/login | Get an authentication token


# **login**
> AuthenticationResponse login(authentication_request)

Get an authentication token

Returns an authentication token that your Toast API client can present
when using other Toast platform APIs.


### Example


```python
import toastapi
from toastapi.models.authentication_request import AuthenticationRequest
from toastapi.models.authentication_response import AuthenticationResponse
from toastapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ws-sandbox-api.eng.toasttab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = toastapi.Configuration(
    host = "https://ws-sandbox-api.eng.toasttab.com"
)


# Enter a context with an instance of the API client
async with toastapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = toastapi.AuthenticationApi(api_client)
    authentication_request = toastapi.AuthenticationRequest() # AuthenticationRequest | The authentication credentials for your Toast API client integration software. 

    try:
        # Get an authentication token
        api_response = await api_instance.login(authentication_request)
        print("The response of AuthenticationApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_request** | [**AuthenticationRequest**](AuthenticationRequest.md)| The authentication credentials for your Toast API client integration software.  | 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON &#x60;AuthenticationResponse&#x60; object that includes an authentication token string.  |  -  |
**401** | The Toast API client credentials in your request are not valid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

