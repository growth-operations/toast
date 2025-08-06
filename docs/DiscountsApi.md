# toastapi.DiscountsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicable_discounts_post**](DiscountsApi.md#applicable_discounts_post) | **POST** /orders/v2/applicableDiscounts | Get applicable discounts
[**discounts_get**](DiscountsApi.md#discounts_get) | **GET** /config/v2/discounts | Get discounts
[**discounts_guid_get**](DiscountsApi.md#discounts_guid_get) | **GET** /config/v2/discounts/{guid} | Get a discount
[**orders_checks_applied_discounts_post**](DiscountsApi.md#orders_checks_applied_discounts_post) | **POST** /orders/v2/orders/{orderGuid}/checks/{checkGuid}/appliedDiscounts | Add check-level discounts
[**orders_checks_selections_applied_discounts_post**](DiscountsApi.md#orders_checks_selections_applied_discounts_post) | **POST** /orders/v2/orders/{orderGuid}/checks/{checkGuid}/selections/{selectionGuid}/appliedDiscounts | Add item-level discounts


# **applicable_discounts_post**
> List[ApplicableDiscount] applicable_discounts_post(toast_restaurant_external_id, applicable_discounts_request)

Get applicable discounts

Returns an array of `ApplicableDiscount`
objects that contain information about the discounts that apply
to the checks and menu item selections in an order.

Each `ApplicableDiscount` object contains information that you can
use to determine which items and checks are eligible for the
discount.

If you include a `promoCode` value in the
`ApplicableDiscount` object, the `applicableDiscounts` endpoint
returns the only the discounts that are associated with that
promotional code.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.applicable_discount import ApplicableDiscount
from toastapi.models.applicable_discounts_request import ApplicableDiscountsRequest
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
    api_instance = toastapi.DiscountsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The identifier of the restaurant.
    applicable_discounts_request = toastapi.ApplicableDiscountsRequest() # ApplicableDiscountsRequest | A JSON `ApplicableDiscountsRequest` object containing information about an order, and an optional `promoCode`. 

    try:
        # Get applicable discounts
        api_response = await api_instance.applicable_discounts_post(toast_restaurant_external_id, applicable_discounts_request)
        print("The response of DiscountsApi->applicable_discounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->applicable_discounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The identifier of the restaurant. | 
 **applicable_discounts_request** | [**ApplicableDiscountsRequest**](ApplicableDiscountsRequest.md)| A JSON &#x60;ApplicableDiscountsRequest&#x60; object containing information about an order, and an optional &#x60;promoCode&#x60;.  | 

### Return type

[**List[ApplicableDiscount]**](ApplicableDiscount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of &#x60;ApplicableDiscount&#x60; objects. |  -  |
**400** | Invalid arguments |  -  |
**500** | An unexpected internal error occurred. The &#x60;requestId&#x60; that is attached to this error can be referenced by Toast. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discounts_get**
> List[Discount] discounts_get(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)

Get discounts

Returns an array of `Discount` objects containing
information about the price deductions configured for a
restaurant. If a `lastModified` date is specified, returns all
objects that were created or modified after that date.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.discount import Discount
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
    api_instance = toastapi.DiscountsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
    page_token = 'page_token_example' # str | A string that identifies the set of data objects that the  endpoint will return in its response data. You can use this  parameter to retrieve one page of response data. You  get the value that you supply in the `pageToken` parameter  from the `Toast-Next-Page-Token` header field value of a  previous request to the endpoint. For more information, see  <a href=\"https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\">Paginating response data</a>.  (optional)
    last_modified = '2013-10-20T19:20:30+01:00' # datetime | Limits the return data to objects created or modified after a specific date and time. For example: `2024-06-20T00:00:00.000%2B0000`.  (optional)

    try:
        # Get discounts
        api_response = await api_instance.discounts_get(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)
        print("The response of DiscountsApi->discounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->discounts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_token** | **str**| A string that identifies the set of data objects that the  endpoint will return in its response data. You can use this  parameter to retrieve one page of response data. You  get the value that you supply in the &#x60;pageToken&#x60; parameter  from the &#x60;Toast-Next-Page-Token&#x60; header field value of a  previous request to the endpoint. For more information, see  &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\&quot;&gt;Paginating response data&lt;/a&gt;.  | [optional] 
 **last_modified** | **datetime**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2024-06-20T00:00:00.000%2B0000&#x60;.  | [optional] 

### Return type

[**List[Discount]**](Discount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of &#x60;Discount&#x60; objects. |  * Toast-Next-Page-Token - A string that identifies the following set of objects that the endpoint will return. You can use this value to retrieve that page of response data. To return the next page of objects you supply this value in the \&quot;pageToken\&quot; parameter of the next request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discounts_guid_get**
> Discount discounts_guid_get(toast_restaurant_external_id, guid)

Get a discount

Returns a `Discount`
object containing information about a price deduction
configured for a restaurant.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.discount import Discount
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
    api_instance = toastapi.DiscountsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
    guid = 'guid_example' # str | The Toast POS GUID of the discount.

    try:
        # Get a discount
        api_response = await api_instance.discounts_guid_get(toast_restaurant_external_id, guid)
        print("The response of DiscountsApi->discounts_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->discounts_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the discount. | 

### Return type

[**Discount**](Discount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a &#x60;Discount&#x60; object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_checks_applied_discounts_post**
> Order orders_checks_applied_discounts_post(order_guid, check_guid, applied_discount)

Add check-level discounts

Adds one or more check-level discounts to a check in an
existing order. Include an array of `Discount` objects in the
message body.

For more information, see 
<a href="https://doc.toasttab.com/doc/devguide/apiDiscountingOrders.html#apiAddingDiscountsToChecks">
the _Toast Developer Guide_</a>.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.applied_discount import AppliedDiscount
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
    api_instance = toastapi.DiscountsApi(api_client)
    order_guid = 'order_guid_example' # str | The Toast platform identifier of the order that you are adding a discount to. 
    check_guid = 'check_guid_example' # str | The Toast platform identifier of the check that you are adding a discount to. 
    applied_discount = [toastapi.AppliedDiscount()] # List[AppliedDiscount] | A JSON array of `AppliedDiscount` objects that identify the discounts you are adding. 

    try:
        # Add check-level discounts
        api_response = await api_instance.orders_checks_applied_discounts_post(order_guid, check_guid, applied_discount)
        print("The response of DiscountsApi->orders_checks_applied_discounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->orders_checks_applied_discounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_guid** | **str**| The Toast platform identifier of the order that you are adding a discount to.  | 
 **check_guid** | **str**| The Toast platform identifier of the check that you are adding a discount to.  | 
 **applied_discount** | [**List[AppliedDiscount]**](AppliedDiscount.md)| A JSON array of &#x60;AppliedDiscount&#x60; objects that identify the discounts you are adding.  | 

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
**200** | A JSON &#x60;Order&#x60; object that includes the discount you added.  |  -  |
**400** | The API cannot process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_checks_selections_applied_discounts_post**
> Order orders_checks_selections_applied_discounts_post(order_guid, check_guid, selection_guid, applied_discount)

Add item-level discounts

Adds one or more item-level discounts to menu item selections
in a check in an existing order. Include an array of `Discount` objects in the
message body.

For more information, see <a
href="https://doc.toasttab.com/doc/devguide/apiDiscountingOrders.html#apiAddingDiscountsToChecks">
the _Toast Developer Guide_</a>.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.applied_discount import AppliedDiscount
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
    api_instance = toastapi.DiscountsApi(api_client)
    order_guid = 'order_guid_example' # str | The Toast platform identifier of the order that you are adding a discount to. 
    check_guid = 'check_guid_example' # str | The Toast platform identifier of the check that you are adding a discount to. 
    selection_guid = 'selection_guid_example' # str | The Toast platform identifier of the menu item selection that you are adding a discount to. 
    applied_discount = [toastapi.AppliedDiscount()] # List[AppliedDiscount] | A JSON array of `AppliedDiscount` objects that identify the discounts you are adding. 

    try:
        # Add item-level discounts
        api_response = await api_instance.orders_checks_selections_applied_discounts_post(order_guid, check_guid, selection_guid, applied_discount)
        print("The response of DiscountsApi->orders_checks_selections_applied_discounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->orders_checks_selections_applied_discounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_guid** | **str**| The Toast platform identifier of the order that you are adding a discount to.  | 
 **check_guid** | **str**| The Toast platform identifier of the check that you are adding a discount to.  | 
 **selection_guid** | **str**| The Toast platform identifier of the menu item selection that you are adding a discount to.  | 
 **applied_discount** | [**List[AppliedDiscount]**](AppliedDiscount.md)| A JSON array of &#x60;AppliedDiscount&#x60; objects that identify the discounts you are adding.  | 

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
**200** | A JSON &#x60;Order&#x60; object that includes the discount you added.  |  -  |
**400** | The API cannot process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

