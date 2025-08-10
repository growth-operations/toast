# toastapi.OrdersApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_bulk_get**](OrdersApi.md#orders_bulk_get) | **GET** /orders/v2/ordersBulk | Get multiple orders
[**orders_get**](OrdersApi.md#orders_get) | **GET** /orders/v2/orders | Get order identifiers (deprecated)
[**orders_guid_get**](OrdersApi.md#orders_guid_get) | **GET** /orders/v2/orders/{guid} | Get an order
[**orders_order_guid_checks_check_guid_selections_post**](OrdersApi.md#orders_order_guid_checks_check_guid_selections_post) | **POST** /orders/v2/orders/{orderGuid}/checks/{checkGuid}/selections | Add items to a check
[**orders_order_guid_delivery_info_patch**](OrdersApi.md#orders_order_guid_delivery_info_patch) | **PATCH** /orders/v2/orders/{orderGuid}/deliveryInfo | Update delivery information
[**orders_post**](OrdersApi.md#orders_post) | **POST** /orders/v2/orders | Post an order
[**prices_post**](OrdersApi.md#prices_post) | **POST** /orders/v2/prices | Get order prices
[**void_order**](OrdersApi.md#void_order) | **POST** /orders/v2/orders/{orderGuid}/void | Void an order


# **orders_bulk_get**
> List[Order] orders_bulk_get(toast_restaurant_external_id, start_date=start_date, end_date=end_date, business_date=business_date, page_size=page_size, page=page)

Get multiple orders

Returns an array of `Order` objects containing detailed
information about all of the orders opened during a period of time.

You can return the orders for either a specific period of time
or for one business day.

* Specify both `startDate` and `endDate` to return the orders
  modified during that period of time.

* Specify the `businessDate` to return the orders promised
  during that business day.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.order import Order
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
    api_instance = toastapi.OrdersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier for the restaurant that processed the orders. 
    start_date = 'start_date_example' # str | The inclusive start date and time. The results include orders with a modified date and time that occur at or after the `startDate`, but before the `endDate`.  Use ISO-8601 format for the date and time, including a decimal fraction of a second. For example, `2016-01-01T14:13:12.000+0400`. URL encode the date and time value.  The date must be after 2015-12-01T00:00:00.000+0000.  (optional)
    end_date = 'end_date_example' # str | The exclusive end date and time. The results exclude any orders that have a modified date and time that occurs at or after `endDate`.  Use ISO-8601 format for the date and time, including a decimal fraction of a second. For example, `2016-01-01T14:13:12.000+0400`. URL encode the date and time value.  The `endDate` date and time must be later than the `startDate` parameter value.  (optional)
    business_date = 'business_date_example' # str | The business date that same-day orders opened or that scheduled orders are promised, in the format `yyyymmdd`.  The business day of an order is determined by the time the order is opened or promised in the local time zone, and the restaurant's business day cutoff time, which is available from  the `General` object of the restaurants API in the `closeoutHour` property.  (optional)
    page_size = 56 # int | The maximum number of objects to return in the array. If the number of objects selected by your request is greater than the `pageSize`, the API uses response pagination for the remaining objects.  The maximum `pageSize` is `100`.  For more information, see [the _Toast Developer Guide_](https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html).  (optional)
    page = 56 # int | The sequence number of the set of objects to return in paginated response data.  For example, if you set the `pageSize` parameter to `10`, and you set `page` to `2`, the API returns a set of objects that starts with the eleventh object.  For more information, see [the _Toast Developer Guide_](https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html).  (optional)

    try:
        # Get multiple orders
        api_response = await api_instance.orders_bulk_get(toast_restaurant_external_id, start_date=start_date, end_date=end_date, business_date=business_date, page_size=page_size, page=page)
        print("The response of OrdersApi->orders_bulk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_bulk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier for the restaurant that processed the orders.  | 
 **start_date** | **str**| The inclusive start date and time. The results include orders with a modified date and time that occur at or after the &#x60;startDate&#x60;, but before the &#x60;endDate&#x60;.  Use ISO-8601 format for the date and time, including a decimal fraction of a second. For example, &#x60;2016-01-01T14:13:12.000+0400&#x60;. URL encode the date and time value.  The date must be after 2015-12-01T00:00:00.000+0000.  | [optional] 
 **end_date** | **str**| The exclusive end date and time. The results exclude any orders that have a modified date and time that occurs at or after &#x60;endDate&#x60;.  Use ISO-8601 format for the date and time, including a decimal fraction of a second. For example, &#x60;2016-01-01T14:13:12.000+0400&#x60;. URL encode the date and time value.  The &#x60;endDate&#x60; date and time must be later than the &#x60;startDate&#x60; parameter value.  | [optional] 
 **business_date** | **str**| The business date that same-day orders opened or that scheduled orders are promised, in the format &#x60;yyyymmdd&#x60;.  The business day of an order is determined by the time the order is opened or promised in the local time zone, and the restaurant&#39;s business day cutoff time, which is available from  the &#x60;General&#x60; object of the restaurants API in the &#x60;closeoutHour&#x60; property.  | [optional] 
 **page_size** | **int**| The maximum number of objects to return in the array. If the number of objects selected by your request is greater than the &#x60;pageSize&#x60;, the API uses response pagination for the remaining objects.  The maximum &#x60;pageSize&#x60; is &#x60;100&#x60;.  For more information, see [the _Toast Developer Guide_](https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html).  | [optional] 
 **page** | **int**| The sequence number of the set of objects to return in paginated response data.  For example, if you set the &#x60;pageSize&#x60; parameter to &#x60;10&#x60;, and you set &#x60;page&#x60; to &#x60;2&#x60;, the API returns a set of objects that starts with the eleventh object.  For more information, see [the _Toast Developer Guide_](https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html).  | [optional] 

### Return type

[**List[Order]**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of &#x60;Order&#x60; objects for each order processed during the period of time that you specify in your request.  |  -  |
**400** | The request contains data that is not supported by the API.  |  -  |
**500** | An unexpected internal error occurred. The &#x60;requestId&#x60; that is attached to this error can be referenced by the Toast support team.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_get**
> List[str] orders_get(toast_restaurant_external_id, start_date=start_date, end_date=end_date, business_date=business_date)

Get order identifiers (deprecated)

Returns a list of the GUIDs of all orders opened during a period of
time. You can return the list of orders for either a period of up to
one hour or for one business day.
* Specify both `startDate` and `endDate` to return the list of orders
  modified during a period of up to one hour.
* Specify the `businessDate` to return the list of orders promised
  for delivery during a business day.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
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
    api_instance = toastapi.OrdersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier for the restaurant to retrieve orders from.
    start_date = 'start_date_example' # str | \\ The inclusive start date and time. The results exclude orders with an earlier modified date and time. Use ISO-8601 format for the date and time, including a decimal fraction of a second. For example, `2016-01-01T14:13:12.000+0400`. URL encode the date and time value. The date must be after 2015-12-01T00:00:00.000+0000. (optional)
    end_date = 'end_date_example' # str |  The exclusive end date and time. The results exclude orders with an equal or later modified date and time.  Use ISO-8601 format for the date and time, including a decimal fraction of a second. For example, `2016-01-01T14:13:12.000+0400`. URL encode the date and time value.  The `endDate` date and time must be later than the `startDate` parameter value.  (optional)
    business_date = 'business_date_example' # str | The business date that same-day orders opened or that scheduled orders are promised, in the format `yyyyMMdd`.  The business day of an order is determined by the time the order is opened or promised in the local time zone, and by the restaurant's business day cutoff time, which is available from  the `General` object of the restaurants API in the `closeoutHour` property.  (optional)

    try:
        # Get order identifiers (deprecated)
        api_response = await api_instance.orders_get(toast_restaurant_external_id, start_date=start_date, end_date=end_date, business_date=business_date)
        print("The response of OrdersApi->orders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier for the restaurant to retrieve orders from. | 
 **start_date** | **str**| \\ The inclusive start date and time. The results exclude orders with an earlier modified date and time. Use ISO-8601 format for the date and time, including a decimal fraction of a second. For example, &#x60;2016-01-01T14:13:12.000+0400&#x60;. URL encode the date and time value. The date must be after 2015-12-01T00:00:00.000+0000. | [optional] 
 **end_date** | **str**|  The exclusive end date and time. The results exclude orders with an equal or later modified date and time.  Use ISO-8601 format for the date and time, including a decimal fraction of a second. For example, &#x60;2016-01-01T14:13:12.000+0400&#x60;. URL encode the date and time value.  The &#x60;endDate&#x60; date and time must be later than the &#x60;startDate&#x60; parameter value.  | [optional] 
 **business_date** | **str**| The business date that same-day orders opened or that scheduled orders are promised, in the format &#x60;yyyyMMdd&#x60;.  The business day of an order is determined by the time the order is opened or promised in the local time zone, and by the restaurant&#39;s business day cutoff time, which is available from  the &#x60;General&#x60; object of the restaurants API in the &#x60;closeoutHour&#x60; property.  | [optional] 

### Return type

**List[str]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of the GUID identifiers for orders. |  -  |
**400** | The request contains data that is not supported by the current version of the API as described. For example, specifying credit card as the payment type. |  -  |
**500** | An unexpected internal error occurred. The &#x60;requestId&#x60; that is attached to this error can be referenced by Toast. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_guid_get**
> Order orders_guid_get(toast_restaurant_external_id, guid)

Get an order

Retrieves detailed information about a single order, specified by its GUID.

### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.order import Order
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
    api_instance = toastapi.OrdersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier of the restaurant where this order was placed.
    guid = 'guid_example' # str | The GUID for the order to be returned.

    try:
        # Get an order
        api_response = await api_instance.orders_guid_get(toast_restaurant_external_id, guid)
        print("The response of OrdersApi->orders_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier of the restaurant where this order was placed. | 
 **guid** | **str**| The GUID for the order to be returned. | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON Order object. |  -  |
**400** | The GUID was malformed. |  -  |
**404** | The specified order was not found. |  -  |
**500** | There was a problem serializing the order entity. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_order_guid_checks_check_guid_selections_post**
> Order orders_order_guid_checks_check_guid_selections_post(toast_restaurant_external_id, order_guid, check_guid, selection)

Add items to a check

Adds one or more items to an existing check in an order.

Include information about the items in an array of `Selection` objects in the
message body.

Specify the Toast platform GUID of the order and
check in REST path parameters.

For more information, see 
<a href="https://doc.toasttab.com/doc/devguide/apiAddingItemsToACheck.html">the 
_Toast Developer Guide_</a>.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.order import Order
from toastapi.models.selection import Selection
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
    api_instance = toastapi.OrdersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier of the restaurant.
    order_guid = 'order_guid_example' # str | The Toast platform identifier of the order that you are adding items to. 
    check_guid = 'check_guid_example' # str | The Toast platform identifier of the check that you are adding items to. 
    selection = [toastapi.Selection()] # List[Selection] | An array of JSON `Selection` objects that identify the menu items you are adding. 

    try:
        # Add items to a check
        api_response = await api_instance.orders_order_guid_checks_check_guid_selections_post(toast_restaurant_external_id, order_guid, check_guid, selection)
        print("The response of OrdersApi->orders_order_guid_checks_check_guid_selections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_order_guid_checks_check_guid_selections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier of the restaurant. | 
 **order_guid** | **str**| The Toast platform identifier of the order that you are adding items to.  | 
 **check_guid** | **str**| The Toast platform identifier of the check that you are adding items to.  | 
 **selection** | [**List[Selection]**](Selection.md)| An array of JSON &#x60;Selection&#x60; objects that identify the menu items you are adding.  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The response body contains the full order JSON, including the &#x60;Selection&#x60; objects with the items from the original check and the newly added ones you included.  |  -  |
**400** | The request contains data that is not supported by the API.  |  -  |
**404** | An entity referenced in the order does not exist at the restaurant.  |  -  |
**500** | An unexpected internal error occurred. The &#x60;requestId&#x60; that is attached to this error can be referenced by the Toast support team.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_order_guid_delivery_info_patch**
> Order orders_order_guid_delivery_info_patch(toast_restaurant_external_id, order_guid, orders_order_guid_delivery_info_patch_request)

Update delivery information

Updates the delivery information of an order that uses the `DELIVERY` dining option.
You can use this endpoint to update the delivery time, dispatch time, the
employee who is delivering the order, the delivery state, or a
combination of the four.

Specify the Toast platform GUID of the
order in the `PATCH` path parameters. Returns a JSON
`Order` object if successful.

For more information, see 
<a href="https://doc.toasttab.com/doc/devguide/apiUpdatingDeliveryInfoForAnOrder.html">
the _Toast Developer Guide_</a>.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.order import Order
from toastapi.models.orders_order_guid_delivery_info_patch_request import OrdersOrderGuidDeliveryInfoPatchRequest
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
    api_instance = toastapi.OrdersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier of the restaurant.
    order_guid = 'order_guid_example' # str | The Toast platform identifier of the order that you are updating the delivery information for. 
    orders_order_guid_delivery_info_patch_request = toastapi.OrdersOrderGuidDeliveryInfoPatchRequest() # OrdersOrderGuidDeliveryInfoPatchRequest | A JSON `deliveryInfo` object containing the delivery information you want to update for an order.  You can update the `deliveredDate`, `dispatchedDate`, `deliveryState`, or `DeliveryEmployee`.  These are the only values you can update with this endpoint. 

    try:
        # Update delivery information
        api_response = await api_instance.orders_order_guid_delivery_info_patch(toast_restaurant_external_id, order_guid, orders_order_guid_delivery_info_patch_request)
        print("The response of OrdersApi->orders_order_guid_delivery_info_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_order_guid_delivery_info_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier of the restaurant. | 
 **order_guid** | **str**| The Toast platform identifier of the order that you are updating the delivery information for.  | 
 **orders_order_guid_delivery_info_patch_request** | [**OrdersOrderGuidDeliveryInfoPatchRequest**](OrdersOrderGuidDeliveryInfoPatchRequest.md)| A JSON &#x60;deliveryInfo&#x60; object containing the delivery information you want to update for an order.  You can update the &#x60;deliveredDate&#x60;, &#x60;dispatchedDate&#x60;, &#x60;deliveryState&#x60;, or &#x60;DeliveryEmployee&#x60;.  These are the only values you can update with this endpoint.  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The response body contains the full order JSON, including information you updated in the &#x60;deliveryInfo&#x60; object. |  -  |
**400** | The request contains data that is not supported by the API.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_post**
> OrderResponse orders_post(toast_restaurant_external_id, order)

Post an order

Submits an order to the server. Returns a JSON `Order` object if successful.

### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.order import Order
from toastapi.models.order_response import OrderResponse
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
    api_instance = toastapi.OrdersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier for the restaurant where this order was placed.
    order = toastapi.Order() # Order | A JSON object containing information about an order.

    try:
        # Post an order
        api_response = await api_instance.orders_post(toast_restaurant_external_id, order)
        print("The response of OrdersApi->orders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier for the restaurant where this order was placed. | 
 **order** | [**Order**](Order.md)| A JSON object containing information about an order. | 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON &#x60;Order&#x60; object that has been persisted in Toast. The returned Order contains generated property values for the check amounts, taxes, service charges, and GUIDs for persisted entities. |  -  |
**400** | Either the request contains data that is not supported by the current version of the API as described (e.g. specifying credit card as the payment type.), or the order contains an item that is negatively priced. |  -  |
**404** | An entity referenced in the order does not exist, or belongs to a restaurant the authenticated client is not authorized to access. |  -  |
**413** | The number of checks in the submitted order exceeds the limit. |  -  |
**415** | The request did not have \&quot;application/json\&quot; in the Content-Type header. |  -  |
**500** | An unexpected internal error occurred. There is a requestId attached to this error that can be referenced by Toast. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prices_post**
> Order prices_post(toast_restaurant_external_id, order)

Get order prices

Calculates the check price amounts, tax amounts, and service
charges for an `Order` object you supply as a _required message
body parameter_.

The `prices` endpoint validates the order you
submit to ensure all referenced data exists and that you include
item selections in the expected structure with all required modifier
options.

Some values that would be present in the response data when
creating an order are not present in the response data for the `prices`
endpoint. For example, the order GUID is not set because the
Toast platform does not create persistent data for the order.

The calculated price can change between requests to the
`prices` endpoint with the same `Order` object if enough time
passes between the requests. The difference in price is
possible because the restaurant configuration can change and
because some pricing configuration is based on time and date
schedules.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.order import Order
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
    api_instance = toastapi.OrdersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier of the restaurant to be used for this price calculation. 
    order = toastapi.Order() # Order | A _required_ JSON `Order` object containing information about the checks, item selections, modifier options, and other parts of the order. 

    try:
        # Get order prices
        api_response = await api_instance.prices_post(toast_restaurant_external_id, order)
        print("The response of OrdersApi->prices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->prices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier of the restaurant to be used for this price calculation.  | 
 **order** | [**Order**](Order.md)| A _required_ JSON &#x60;Order&#x60; object containing information about the checks, item selections, modifier options, and other parts of the order.  | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The response body contains a JSON &#x60;Order&#x60; object with values for check amounts, taxes, service charges, and other parts of the order.  Because this endpoint only calculates prices, no parts of the order persist in the Toast platform. There are no GUIDs in the response object.  |  -  |
**400** | Either the request contains data that is not supported by the current version of the API as described, or the order contains an item that is negatively priced.  |  -  |
**403** | The API client does not have access to the restaurant, the API client does not have the &#x60;orders:read&#x60; scope, or both.  |  -  |
**404** | An entity referenced in the order does not exist, or belongs to a restaurant that the API client is not authorized to access.  |  -  |
**413** | The number of checks in the submitted order exceeds the limit.  |  -  |
**415** | The request did not have &#x60;application/json&#x60; in the &#x60;Content-Type&#x60; HTTP header field.  |  -  |
**500** | An unexpected internal error occurred. The &#x60;requestId&#x60; that is attached to the error can be referenced by the Toast support team.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_order**
> Order void_order(toast_restaurant_external_id, order_guid, void_order_request=void_order_request)

Void an order

Voids an order, and (if specified) its selections and payments. Only Orders with `OTHER` payment types can be voided.

A request body that contains the `selections` and `payments` objects with each `voidAll` value set to `true` is required to void an order. The response body is the modified Order object.

For more information, see [Void an order](https://doc.toasttab.com/doc/devguide/apiVoidOrder.html).


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.order import Order
from toastapi.models.void_order_request import VoidOrderRequest
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
    api_instance = toastapi.OrdersApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier of the restaurant.
    order_guid = 'order_guid_example' # str | The GUID of the order to be voided.
    void_order_request = toastapi.VoidOrderRequest() # VoidOrderRequest |  (optional)

    try:
        # Void an order
        api_response = await api_instance.void_order(toast_restaurant_external_id, order_guid, void_order_request=void_order_request)
        print("The response of OrdersApi->void_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->void_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier of the restaurant. | 
 **order_guid** | **str**| The GUID of the order to be voided. | 
 **void_order_request** | [**VoidOrderRequest**](VoidOrderRequest.md)|  | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modified order object. |  -  |
**400** | Malformed order GUID or other validation errors.  |  -  |
**404** | Order not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

