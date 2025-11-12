# toastapi.SalesCategoriesApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sales_category_by_id**](SalesCategoriesApi.md#get_sales_category_by_id) | **GET** /config/v2/salesCategories/{guid} | Get a menu item sales category
[**list_sales_categories**](SalesCategoriesApi.md#list_sales_categories) | **GET** /config/v2/salesCategories | Get menu item sales categories


# **get_sales_category_by_id**
> SalesCategory get_sales_category_by_id(toast_restaurant_external_id, guid)

Get a menu item sales category

Returns a `SalesCategory` object
containing information about a type of menu item used to
analyze purchases at a restaurant. For example, food and
alcohol might be sales categories for a restaurant.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.sales_category import SalesCategory
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
    api_instance = toastapi.SalesCategoriesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
    guid = 'guid_example' # str | The Toast POS GUID of the sales category.

    try:
        # Get a menu item sales category
        api_response = await api_instance.get_sales_category_by_id(toast_restaurant_external_id, guid)
        print("The response of SalesCategoriesApi->get_sales_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesCategoriesApi->get_sales_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the sales category. | 

### Return type

[**SalesCategory**](SalesCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a &#x60;SalesCategory&#x60; object. |  -  |
**404** | Sales category not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_categories**
> List[SalesCategory] list_sales_categories(toast_restaurant_external_id, limit=limit, page_token=page_token, last_modified=last_modified)

Get menu item sales categories

Returns an array of `SalesCategory` objects
containing information about the types of menu item used to
analyze purchases at a restaurant. For example, food and
alcohol might be sales categories for a restaurant. If a
`lastModified` date is specified, returns all objects that were
created or modified after that date.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.sales_category import SalesCategory
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
    api_instance = toastapi.SalesCategoriesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
    limit = 300 # int | The maximum number of objects to return. The default value is 300. The maximum value is 300. (optional) (default to 300)
    page_token = 'page_token_example' # str | A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the `pageToken` parameter from the `Toast-Next-Page-Token` header field value of a previous request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html.  (optional)
    last_modified = '2013-10-20T19:20:30+01:00' # datetime | Limits the return data to objects created or modified after a specific date and time. For example: `2024-06-20T00:00:00.000+0000`.  (optional)

    try:
        # Get menu item sales categories
        api_response = await api_instance.list_sales_categories(toast_restaurant_external_id, limit=limit, page_token=page_token, last_modified=last_modified)
        print("The response of SalesCategoriesApi->list_sales_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesCategoriesApi->list_sales_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **limit** | **int**| The maximum number of objects to return. The default value is 300. The maximum value is 300. | [optional] [default to 300]
 **page_token** | **str**| A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the &#x60;pageToken&#x60; parameter from the &#x60;Toast-Next-Page-Token&#x60; header field value of a previous request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html.  | [optional] 
 **last_modified** | **datetime**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2024-06-20T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**List[SalesCategory]**](SalesCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of &#x60;SalesCategory&#x60; objects. |  * Toast-Next-Page-Token - A string that identifies the following set of objects that the endpoint will return. You can use this value to retrieve that page of response data. To return the next page of objects you supply this value in the \&quot;pageToken\&quot; parameter of the next request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

