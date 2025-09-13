# toastapi.PaymentsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_payments_to_check**](PaymentsApi.md#add_payments_to_check) | **POST** /orders/v2/orders/{orderGuid}/checks/{checkGuid}/payments | Post payments
[**get_payment_by_guid**](PaymentsApi.md#get_payment_by_guid) | **GET** /orders/v2/payments/{guid} | Get a payment
[**list_payments**](PaymentsApi.md#list_payments) | **GET** /orders/v2/payments | Get payment identifiers
[**update_tip_amount**](PaymentsApi.md#update_tip_amount) | **PATCH** /orders/v2/orders/{orderGuid}/checks/{checkGuid}/payments/{paymentGuid} | Update a tip amount


# **add_payments_to_check**
> Order add_payments_to_check(order_guid, check_guid, payment)

Post payments

Adds one or more payments to a check in an existing order. Include
information about the payments in an array of `Payment` objects in the
message body. Specify the Toast platform GUID of the order
and check in REST path parameters.

For more information, see <a
href="https://doc.toasttab.com/doc/devguide/apiAddingPaymentsToACheck.html">
the _Toast Developer Guide_</a>.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.order import Order
from toastapi.models.payment import Payment
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
    api_instance = toastapi.PaymentsApi(api_client)
    order_guid = 'order_guid_example' # str | The Toast platform identifier of the order that you are adding payments to. 
    check_guid = 'check_guid_example' # str | The Toast platform identifier of the check that you are adding payments to. 
    payment = [toastapi.Payment()] # List[Payment] | An array of JSON `Payment` objects containing information about the payments you are adding. 

    try:
        # Post payments
        api_response = await api_instance.add_payments_to_check(order_guid, check_guid, payment)
        print("The response of PaymentsApi->add_payments_to_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->add_payments_to_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_guid** | **str**| The Toast platform identifier of the order that you are adding payments to.  | 
 **check_guid** | **str**| The Toast platform identifier of the check that you are adding payments to.  | 
 **payment** | [**List[Payment]**](Payment.md)| An array of JSON &#x60;Payment&#x60; objects containing information about the payments you are adding.  | 

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
**200** | A JSON &#x60;Order&#x60; object that includes the payments that you added.  |  -  |
**400** | The API cannot process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_guid**
> Payment get_payment_by_guid(toast_restaurant_external_id, guid)

Get a payment

Returns a JSON `Payment` object containing detailed information about a  single payment, specified by its GUID.

### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.payment import Payment
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
    api_instance = toastapi.PaymentsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The GUID of the restaurant used as the context of the request.
    guid = 'guid_example' # str | The GUID for the payment you want to return.

    try:
        # Get a payment
        api_response = await api_instance.get_payment_by_guid(toast_restaurant_external_id, guid)
        print("The response of PaymentsApi->get_payment_by_guid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payment_by_guid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The GUID of the restaurant used as the context of the request. | 
 **guid** | **str**| The GUID for the payment you want to return. | 

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a JSON &#x60;Payment&#x60; object. |  -  |
**400** | The GUID was malformed. |  -  |
**404** | The specified payment was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payments**
> List[str] list_payments(toast_restaurant_external_id, paid_business_date=paid_business_date, refund_business_date=refund_business_date, void_business_date=void_business_date)

Get payment identifiers

Returns a list of the GUIDs for each payment made during
one restaurant business day.

The specific hours that make up a business
day depend on the business day cutoff in the restaurant configuration,
which is available from the restaurants API in the `closeoutHour`
property.

The business day for a restaurant is based on its local time (not UTC
or local time for an API client).

You must include one of the
`paidBusinessDate`, `refundBusinessDate`, or `voidBusinessDate` query
parameters.


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
    api_instance = toastapi.PaymentsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The GUID of the restaurant used as the context of the request.
    paid_business_date = 'paid_business_date_example' # str | Returns a list of the payments that were made during one business day. Specify the business day in the format yyyyMMdd. For example, `20170101`.  (optional)
    refund_business_date = 'refund_business_date_example' # str | Returns a list of the payments that were refunded during one business day. Specify the business day in the format yyyyMMdd. For example, `20170101`.  (optional)
    void_business_date = 'void_business_date_example' # str | Returns a list of the payments that were voided during one business day. Specify the business day in the format yyyyMMdd. For example, `20170101`.  (optional)

    try:
        # Get payment identifiers
        api_response = await api_instance.list_payments(toast_restaurant_external_id, paid_business_date=paid_business_date, refund_business_date=refund_business_date, void_business_date=void_business_date)
        print("The response of PaymentsApi->list_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->list_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The GUID of the restaurant used as the context of the request. | 
 **paid_business_date** | **str**| Returns a list of the payments that were made during one business day. Specify the business day in the format yyyyMMdd. For example, &#x60;20170101&#x60;.  | [optional] 
 **refund_business_date** | **str**| Returns a list of the payments that were refunded during one business day. Specify the business day in the format yyyyMMdd. For example, &#x60;20170101&#x60;.  | [optional] 
 **void_business_date** | **str**| Returns a list of the payments that were voided during one business day. Specify the business day in the format yyyyMMdd. For example, &#x60;20170101&#x60;.  | [optional] 

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
**200** | A JSON array of the GUID identifiers for the payments. |  -  |
**400** | The API cannot process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tip_amount**
> Order update_tip_amount(order_guid, check_guid, payment_guid, update_payment_request)

Update a tip amount

Updates the tip amount in an existing payment for a check in an
order. Include the new `tipAmount` value in a `Payment` object
in the message body.

This endpoint does not allow any other
`Payment` object value for a `PATCH` request.

Specify the Toast
platform GUID of the order, check, and payment in REST path
parameters.

For more information, see <a
href="https://doc.toasttab.com/doc/devguide/apiUpdatingTipsInAPayment.html">
the _Toast Developer Guide_</a>.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.order import Order
from toastapi.models.update_payment_request import UpdatePaymentRequest
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
    api_instance = toastapi.PaymentsApi(api_client)
    order_guid = 'order_guid_example' # str | The Toast platform identifier of the order that you are updating a tip in. 
    check_guid = 'check_guid_example' # str | The Toast platform identifier of the check that you are updating a tip in. 
    payment_guid = 'payment_guid_example' # str | The Toast platform identifier of the payment that you are updating a tip in. 
    update_payment_request = toastapi.UpdatePaymentRequest() # UpdatePaymentRequest | A JSON `Payment` object containing the `tipAmount` value that will replace any existing tip amount for the payment.  Do not include any value other than `tipAmount`. 

    try:
        # Update a tip amount
        api_response = await api_instance.update_tip_amount(order_guid, check_guid, payment_guid, update_payment_request)
        print("The response of PaymentsApi->update_tip_amount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->update_tip_amount: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_guid** | **str**| The Toast platform identifier of the order that you are updating a tip in.  | 
 **check_guid** | **str**| The Toast platform identifier of the check that you are updating a tip in.  | 
 **payment_guid** | **str**| The Toast platform identifier of the payment that you are updating a tip in.  | 
 **update_payment_request** | [**UpdatePaymentRequest**](UpdatePaymentRequest.md)| A JSON &#x60;Payment&#x60; object containing the &#x60;tipAmount&#x60; value that will replace any existing tip amount for the payment.  Do not include any value other than &#x60;tipAmount&#x60;.  | 

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
**200** | A JSON &#x60;Order&#x60; object that includes the tip amount that you updated.  |  -  |
**400** | The API cannot process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

