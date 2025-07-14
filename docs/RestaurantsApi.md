# toastapi.RestaurantsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_management_group_guid_restaurants_get**](RestaurantsApi.md#groups_management_group_guid_restaurants_get) | **GET** /restaurants/v1/groups/{managementGroupGUID}/restaurants | Get restaurants in a management group
[**restaurants_restaurant_guid_get**](RestaurantsApi.md#restaurants_restaurant_guid_get) | **GET** /restaurants/v1/restaurants/{restaurantGUID} | Get restaurant configuration information


# **groups_management_group_guid_restaurants_get**
> List[RestaurantBasic] groups_management_group_guid_restaurants_get(management_group_guid, toast_restaurant_external_id)

Get restaurants in a management group

Returns an array of `Restaurant` objects that are a part of the 
restaurant management group you specify in the 
`managementGroupGUID` path parameter. Each `Restaurant` object 
contains the unique Toast platform identifier for the restaurant in 
its `guid` value.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.restaurant_basic import RestaurantBasic
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
    api_instance = toastapi.RestaurantsApi(api_client)
    management_group_guid = 'management_group_guid_example' # str | The GUID of the restaurant management group. 
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast GUID of one restaurant location in the management  group. 

    try:
        # Get restaurants in a management group
        api_response = await api_instance.groups_management_group_guid_restaurants_get(management_group_guid, toast_restaurant_external_id)
        print("The response of RestaurantsApi->groups_management_group_guid_restaurants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->groups_management_group_guid_restaurants_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **management_group_guid** | **str**| The GUID of the restaurant management group.  | 
 **toast_restaurant_external_id** | **str**| The Toast GUID of one restaurant location in the management  group.  | 

### Return type

[**List[RestaurantBasic]**](RestaurantBasic.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of &#x60;Restaurant&#x60; objects.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restaurants_restaurant_guid_get**
> RestaurantInfo restaurants_restaurant_guid_get(restaurant_guid, toast_restaurant_external_id, include_archived=include_archived)

Get restaurant configuration information

Returns a `RestaurantInfo` object
that contains detailed information about the configuration of a
restaurant.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.restaurant_info import RestaurantInfo
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
    api_instance = toastapi.RestaurantsApi(api_client)
    restaurant_guid = 'restaurant_guid_example' # str | The Toast GUID of the restaurant that you want to get  information about. 
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast GUID of the restaurant that you want to get  information about. 
    include_archived = False # bool | Set `includeArchived` to `true` if the API should return information about the restaurant even if it is archived. The `General` object in the response includes an `archived` value that your integration can use to determine whether a restaurant is archived or not. A common reason for a restaurant being archived is if it was created in error. Set `includeArchived` to `false` if the API should _not_ return information about the restaurant if it is archived. Defaults to `false` if omitted.  (optional) (default to False)

    try:
        # Get restaurant configuration information
        api_response = await api_instance.restaurants_restaurant_guid_get(restaurant_guid, toast_restaurant_external_id, include_archived=include_archived)
        print("The response of RestaurantsApi->restaurants_restaurant_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->restaurants_restaurant_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant_guid** | **str**| The Toast GUID of the restaurant that you want to get  information about.  | 
 **toast_restaurant_external_id** | **str**| The Toast GUID of the restaurant that you want to get  information about.  | 
 **include_archived** | **bool**| Set &#x60;includeArchived&#x60; to &#x60;true&#x60; if the API should return information about the restaurant even if it is archived. The &#x60;General&#x60; object in the response includes an &#x60;archived&#x60; value that your integration can use to determine whether a restaurant is archived or not. A common reason for a restaurant being archived is if it was created in error. Set &#x60;includeArchived&#x60; to &#x60;false&#x60; if the API should _not_ return information about the restaurant if it is archived. Defaults to &#x60;false&#x60; if omitted.  | [optional] [default to False]

### Return type

[**RestaurantInfo**](RestaurantInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A &#x60;RestaurantInfo&#x60; object that contains detailed  information about the configuration of a restaurant.  |  -  |
**404** | If the restaurant GUID you provided is invalid, the API will return an HTTP 404 response. The API will also return an HTTP 404 response if you provided the GUID of an archived restaurant and you have not set the &#x60;includeArchived&#x60; query parameter to &#x60;true&#x60;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

