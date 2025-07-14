# toastapi.ShiftsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shifts_get**](ShiftsApi.md#shifts_get) | **GET** /labor/v1/shifts | Get shifts
[**shifts_post**](ShiftsApi.md#shifts_post) | **POST** /labor/v1/shifts | Create a shift
[**shifts_shift_id_delete**](ShiftsApi.md#shifts_shift_id_delete) | **DELETE** /labor/v1/shifts/{shiftId} | Delete a shift
[**shifts_shift_id_get**](ShiftsApi.md#shifts_shift_id_get) | **GET** /labor/v1/shifts/{shiftId} | Get a shift
[**shifts_shift_id_put**](ShiftsApi.md#shifts_shift_id_put) | **PUT** /labor/v1/shifts/{shiftId} | Update a shift


# **shifts_get**
> List[Shift] shifts_get(toast_restaurant_external_id, shift_ids=shift_ids, start_date=start_date, end_date=end_date)

Get shifts

Returns an array of `Shift` objects that contain information 
about schedule shifts for restaurant employees.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.shift import Shift
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
    api_instance = toastapi.ShiftsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    shift_ids = 'shift_ids_example' # str | An optional identifier that filters return values for a specific shift. The identifier can be a Toast platform GUID or an external identifier. If present, the shifts resource will only return the shifts you specify. You can include multiple `shiftIds` query parameters (maximum 100).  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Optional start date and time of time period to match  shifts. A shift matches the time period if the shift  `inDate` is after (inclusive) the specified `startDate` and  the shift `outDate` is before the `endDate` (exclusive).  These parameters are required if the `shiftIds` parameter  is not defined. The specified period cannot be longer than  one month.  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Optional end date and time of time period to match shifts.  A shift matches the time period if the shift `inDate` is  after (inclusive) the specified `startDate` and the shift  `outDate` is before the `endDate` (exclusive). These  parameters are required if the `shiftIds` parameter is not  defined. The specified period cannot be longer than one  month.  (optional)

    try:
        # Get shifts
        api_response = await api_instance.shifts_get(toast_restaurant_external_id, shift_ids=shift_ids, start_date=start_date, end_date=end_date)
        print("The response of ShiftsApi->shifts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->shifts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **shift_ids** | **str**| An optional identifier that filters return values for a specific shift. The identifier can be a Toast platform GUID or an external identifier. If present, the shifts resource will only return the shifts you specify. You can include multiple &#x60;shiftIds&#x60; query parameters (maximum 100).  | [optional] 
 **start_date** | **datetime**| Optional start date and time of time period to match  shifts. A shift matches the time period if the shift  &#x60;inDate&#x60; is after (inclusive) the specified &#x60;startDate&#x60; and  the shift &#x60;outDate&#x60; is before the &#x60;endDate&#x60; (exclusive).  These parameters are required if the &#x60;shiftIds&#x60; parameter  is not defined. The specified period cannot be longer than  one month.  | [optional] 
 **end_date** | **datetime**| Optional end date and time of time period to match shifts.  A shift matches the time period if the shift &#x60;inDate&#x60; is  after (inclusive) the specified &#x60;startDate&#x60; and the shift  &#x60;outDate&#x60; is before the &#x60;endDate&#x60; (exclusive). These  parameters are required if the &#x60;shiftIds&#x60; parameter is not  defined. The specified period cannot be longer than one  month.  | [optional] 

### Return type

[**List[Shift]**](Shift.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified shifts in an unordered list.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shifts_post**
> Shift shifts_post(toast_restaurant_external_id, content_type, body)

Create a shift

Creates a schedule shift for a restaurant employee.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.shift import Shift
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
    api_instance = toastapi.ShiftsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 
    body = 'body_example' # str | A `Shift` object containing information about the shift,  including the job identifier, the employee identifier, and  the start and end times. 

    try:
        # Create a shift
        api_response = await api_instance.shifts_post(toast_restaurant_external_id, content_type, body)
        print("The response of ShiftsApi->shifts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->shifts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 
 **body** | **str**| A &#x60;Shift&#x60; object containing information about the shift,  including the job identifier, the employee identifier, and  the start and end times.  | 

### Return type

[**Shift**](Shift.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creates a shift record and returns information about it.  |  -  |
**400** | The request contains data that is not supported by the  current version of the API as described.  |  -  |
**415** | The request did not have \&quot;application/json\&quot; in the  &#x60;Content-Type&#x60; header.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shifts_shift_id_delete**
> Shift shifts_shift_id_delete(toast_restaurant_external_id, shift_id)

Delete a shift

Marks an existing schedule shift record for a restaurant 
employee as deleted. If the shift record was already deleted, 
then the operation will succeed (HTTP 200 response code) and no 
change will be made.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.shift import Shift
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
    api_instance = toastapi.ShiftsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    shift_id = 'shift_id_example' # str | The shift identifier, either the Toast platform GUID or an  external identifier. 

    try:
        # Delete a shift
        api_response = await api_instance.shifts_shift_id_delete(toast_restaurant_external_id, shift_id)
        print("The response of ShiftsApi->shifts_shift_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->shifts_shift_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **shift_id** | **str**| The shift identifier, either the Toast platform GUID or an  external identifier.  | 

### Return type

[**Shift**](Shift.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified shift, with the deleted flag set to  &#x60;true&#x60;.  |  -  |
**400** | The Toast platform GUID or external identifier was  malformed.  |  -  |
**404** | The Toast platform GUID or external identifier does not  match any shifts at the current restaurant.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shifts_shift_id_get**
> Shift shifts_shift_id_get(toast_restaurant_external_id, shift_id)

Get a shift

Returns a `Shift` object containing of information about one 
schedule shift for a restaurant employee.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.shift import Shift
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
    api_instance = toastapi.ShiftsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    shift_id = 'shift_id_example' # str | The Toast platform GUID or an external identifier for the  shift. 

    try:
        # Get a shift
        api_response = await api_instance.shifts_shift_id_get(toast_restaurant_external_id, shift_id)
        print("The response of ShiftsApi->shifts_shift_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->shifts_shift_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **shift_id** | **str**| The Toast platform GUID or an external identifier for the  shift.  | 

### Return type

[**Shift**](Shift.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified shifts in an unordered list.  |  -  |
**400** | The GUID or external identifier was malformed.  |  -  |
**404** | The GUID or external identifier does not match any shifts at the current restaurant.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shifts_shift_id_put**
> Shift shifts_shift_id_put(toast_restaurant_external_id, shift_id, body)

Update a shift

Updates an existing schedule shift record for a restaurant 
employee. A `PUT` request completely replaces the information 
in the existing record.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.shift import Shift
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
    api_instance = toastapi.ShiftsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    shift_id = 'shift_id_example' # str | The shift identifier, either the Toast platform GUID or an  external identifier. 
    body = 'body_example' # str | The shift information. The `externalId` identifier is not  allowed for`PUT` requests. 

    try:
        # Update a shift
        api_response = await api_instance.shifts_shift_id_put(toast_restaurant_external_id, shift_id, body)
        print("The response of ShiftsApi->shifts_shift_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->shifts_shift_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **shift_id** | **str**| The shift identifier, either the Toast platform GUID or an  external identifier.  | 
 **body** | **str**| The shift information. The &#x60;externalId&#x60; identifier is not  allowed for&#x60;PUT&#x60; requests.  | 

### Return type

[**Shift**](Shift.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated &#x60;Shift&#x60;.  |  -  |
**400** | The request contains data that is not supported by the  current version of the API as described.  |  -  |
**404** | The GUID or external identifier does not match any shifts at the current restaurant.  |  -  |
**415** | The request did not have &#x60;application/json&#x60; in the  &#x60;Content-Type&#x60; header.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

