# toastapi.ModifierGroupsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_menu_option_group_by_id**](ModifierGroupsApi.md#get_menu_option_group_by_id) | **GET** /config/v2/menuOptionGroups/{guid} | Get a modifier group 
[**list_menu_option_groups**](ModifierGroupsApi.md#list_menu_option_groups) | **GET** /config/v2/menuOptionGroups | Get modifier groups 


# **get_menu_option_group_by_id**
> MenuOptionGroup get_menu_option_group_by_id(toast_restaurant_external_id, guid)

Get a modifier group 

Returns a `MenuOptionGroup` object containing information about a modifier group. For example, salad dressings might be a modifier group for a salad menu item.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.menu_option_group import MenuOptionGroup
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
    api_instance = toastapi.ModifierGroupsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
    guid = 'guid_example' # str | The Toast POS GUID of the modifier group.

    try:
        # Get a modifier group 
        api_response = await api_instance.get_menu_option_group_by_id(toast_restaurant_external_id, guid)
        print("The response of ModifierGroupsApi->get_menu_option_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModifierGroupsApi->get_menu_option_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **guid** | **str**| The Toast POS GUID of the modifier group. | 

### Return type

[**MenuOptionGroup**](MenuOptionGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a &#x60;MenuOptionGroup&#x60; object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_menu_option_groups**
> List[MenuOptionGroup] list_menu_option_groups(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)

Get modifier groups 

Returns an array of `MenuOptionGroup` objects containing information about modifier groups. For example, salad dressings might be a modifier group for a salad menu item.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.menu_option_group import MenuOptionGroup
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
    api_instance = toastapi.ModifierGroupsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast POS GUID of the restaurant that the configuration applies to. 
    page_token = 'page_token_example' # str | A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the `pageToken` parameter from the `Toast-Next-Page-Token` header field value of a previous request to the endpoint. For more information, see <a href=\"https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\">Paginating response data</a>.  (optional)
    last_modified = '2024-06-20T00:00:00.000+0000' # str | Limits the return data to objects created or modified after a specific date and time. For example: `2024-06-20T00:00:00.000+0000`.  (optional)

    try:
        # Get modifier groups 
        api_response = await api_instance.list_menu_option_groups(toast_restaurant_external_id, page_token=page_token, last_modified=last_modified)
        print("The response of ModifierGroupsApi->list_menu_option_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModifierGroupsApi->list_menu_option_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast POS GUID of the restaurant that the configuration applies to.  | 
 **page_token** | **str**| A string that identifies the set of data objects that the endpoint will return in its response data. You can use this parameter to retrieve one page of response data. You get the value that you supply in the &#x60;pageToken&#x60; parameter from the &#x60;Toast-Next-Page-Token&#x60; header field value of a previous request to the endpoint. For more information, see &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html\&quot;&gt;Paginating response data&lt;/a&gt;.  | [optional] 
 **last_modified** | **str**| Limits the return data to objects created or modified after a specific date and time. For example: &#x60;2024-06-20T00:00:00.000+0000&#x60;.  | [optional] 

### Return type

[**List[MenuOptionGroup]**](MenuOptionGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of &#x60;MenuOptionGroup&#x60; objects. |  * Toast-Next-Page-Token - A string that identifies the following set of objects that the endpoint will return. You can use this value to retrieve that page of response data. To return the next page of objects you supply this value in the \&quot;pageToken\&quot; parameter of the next request to the endpoint. For more information, see https://doc.toasttab.com/doc/devguide/apiResponseDataPagination.html. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

