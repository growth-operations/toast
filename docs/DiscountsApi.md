# toastapi.DiscountsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicable_discounts_post**](DiscountsApi.md#applicable_discounts_post) | **POST** /orders/v2/applicableDiscounts | Get applicable discounts
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

