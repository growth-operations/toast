# toastapi.TimeEntriesApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_time_entry_by_id**](TimeEntriesApi.md#get_time_entry_by_id) | **GET** /labor/v1/timeEntries/{timeEntryId} | Get one time entry
[**list_time_entries**](TimeEntriesApi.md#list_time_entries) | **GET** /labor/v1/timeEntries | Get time entries


# **get_time_entry_by_id**
> TimeEntry get_time_entry_by_id(toast_restaurant_external_id, time_entry_id, include_missed_breaks=include_missed_breaks, include_archived=include_archived)

Get one time entry

Returns a `TimeEntry` object containing information about one 
employee shift. The information includes the shift start time, 
end time, and the start and end times of break periods.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.time_entry import TimeEntry
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
    api_instance = toastapi.TimeEntriesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    time_entry_id = 'time_entry_id_example' # str | The Toast platform GUID or an external identifier for the  time entry. 
    include_missed_breaks = True # bool | Optional flag to indicate whether missed breaks should be  returned in the breaks array for the time entries.  (optional)
    include_archived = True # bool | Controls whether the response includes an archived time entry. Optional.  (optional)

    try:
        # Get one time entry
        api_response = await api_instance.get_time_entry_by_id(toast_restaurant_external_id, time_entry_id, include_missed_breaks=include_missed_breaks, include_archived=include_archived)
        print("The response of TimeEntriesApi->get_time_entry_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->get_time_entry_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **time_entry_id** | **str**| The Toast platform GUID or an external identifier for the  time entry.  | 
 **include_missed_breaks** | **bool**| Optional flag to indicate whether missed breaks should be  returned in the breaks array for the time entries.  | [optional] 
 **include_archived** | **bool**| Controls whether the response includes an archived time entry. Optional.  | [optional] 

### Return type

[**TimeEntry**](TimeEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified time entry.  |  -  |
**400** | The GUID or external identifier was malformed.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_entries**
> List[TimeEntry] list_time_entries(toast_restaurant_external_id, time_entry_ids=time_entry_ids, start_date=start_date, end_date=end_date, modified_start_date=modified_start_date, modified_end_date=modified_end_date, business_date=business_date, include_missed_breaks=include_missed_breaks, include_archived=include_archived)

Get time entries

Returns an array of `TimeEntry` objects that contain 
information about employee shift events. The information 
includes shift start times, end times, and the start and end 
times of break periods.

*  Include one or more `timeEntryId` query parameters set to 
   the GUIDs for specific time entries.

*  Include both a `startDate` and an `endDate` query parameter 
   to get time entries for a specific time period.

*  Include both a `modifiedStartDate` and a `modifiedEndDate` 
   query parameter to get the time entries that were modified 
   during a specific time period.

*  Includes a `businessDate` query parameter to get the time 
   entries with an `inDate` during a specific business date.

Valid requests include one or more `timeEntryId` parameters, 
both a `startDate` and an `endDate`, both a `modifiedStartDate` 
and a `modifiedEndDate`, or a `businessDate`.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.time_entry import TimeEntry
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
    api_instance = toastapi.TimeEntriesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    time_entry_ids = ['time_entry_ids_example'] # List[str] | Optional array of one or more time entry identifiers,  either the Toast platform GUID or an external identifier.  100 max.  (optional)
    start_date = 'start_date_example' # str | Optional start date and time of time period to match time  entries. A time entry matches the time period if its  clock-in `inDate` is after (inclusive) the specified  `startDate` and before (exclusive) the `endDate`. The  specified period cannot be longer than one month.  (optional)
    end_date = 'end_date_example' # str | Optional end date and time of time period to match time  entries. A time entry matches the time period if its  clock-in `inDate` is after (inclusive) the specified  `startDate` and before (exclusive) the `endDate`. The  specified period cannot be longer than one month.  (optional)
    modified_start_date = 'modified_start_date_example' # str | Start date and time of the time period to match modified  time entries. A time entry matches the time period if that  entry was modified after (inclusive) the  `modifiedStartDate`. If you include this parameter, you  must also include the `modifiedEndDate` parameter.  The  specified period cannot be longer than one month.  (optional)
    modified_end_date = 'modified_end_date_example' # str | End date and time of the time period to match modified time  entries. A time entry matches the time period if that entry  was modified before (exclusive) the `modifiedEndDate`. If  you include this parameter, you must also include the  `modifiedStartDate` parameter.  The specified period cannot  be longer than one month.  (optional)
    business_date = '2013-10-20' # date | Optional date to match time entries. A time entry matches  the business date if its clock-in `inDate` is during the  business date. The cutoff from one `businessDate` to the  next is the `closeoutHour` for the restaurant.  (optional)
    include_missed_breaks = True # bool | Optional flag to indicate whether missed breaks should be  returned in the breaks array for the time entries.  (optional)
    include_archived = True # bool | Controls whether the response includes archived time entries, when using the `startDate` and `endDate` parameters.  **Important**: this parameter _has no effect_ if you use the `modifiedStartDate` and `modifiedEndDate` parameters or the `businessDate` parameter to select time entries.  * Querying by modified date range _always_ returns archived time entries. * Querying by businessDate _never_ returns archived time entries.  This parameter is optional and the default value is `false`.  (optional)

    try:
        # Get time entries
        api_response = await api_instance.list_time_entries(toast_restaurant_external_id, time_entry_ids=time_entry_ids, start_date=start_date, end_date=end_date, modified_start_date=modified_start_date, modified_end_date=modified_end_date, business_date=business_date, include_missed_breaks=include_missed_breaks, include_archived=include_archived)
        print("The response of TimeEntriesApi->list_time_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->list_time_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **time_entry_ids** | [**List[str]**](str.md)| Optional array of one or more time entry identifiers,  either the Toast platform GUID or an external identifier.  100 max.  | [optional] 
 **start_date** | **str**| Optional start date and time of time period to match time  entries. A time entry matches the time period if its  clock-in &#x60;inDate&#x60; is after (inclusive) the specified  &#x60;startDate&#x60; and before (exclusive) the &#x60;endDate&#x60;. The  specified period cannot be longer than one month.  | [optional] 
 **end_date** | **str**| Optional end date and time of time period to match time  entries. A time entry matches the time period if its  clock-in &#x60;inDate&#x60; is after (inclusive) the specified  &#x60;startDate&#x60; and before (exclusive) the &#x60;endDate&#x60;. The  specified period cannot be longer than one month.  | [optional] 
 **modified_start_date** | **str**| Start date and time of the time period to match modified  time entries. A time entry matches the time period if that  entry was modified after (inclusive) the  &#x60;modifiedStartDate&#x60;. If you include this parameter, you  must also include the &#x60;modifiedEndDate&#x60; parameter.  The  specified period cannot be longer than one month.  | [optional] 
 **modified_end_date** | **str**| End date and time of the time period to match modified time  entries. A time entry matches the time period if that entry  was modified before (exclusive) the &#x60;modifiedEndDate&#x60;. If  you include this parameter, you must also include the  &#x60;modifiedStartDate&#x60; parameter.  The specified period cannot  be longer than one month.  | [optional] 
 **business_date** | **date**| Optional date to match time entries. A time entry matches  the business date if its clock-in &#x60;inDate&#x60; is during the  business date. The cutoff from one &#x60;businessDate&#x60; to the  next is the &#x60;closeoutHour&#x60; for the restaurant.  | [optional] 
 **include_missed_breaks** | **bool**| Optional flag to indicate whether missed breaks should be  returned in the breaks array for the time entries.  | [optional] 
 **include_archived** | **bool**| Controls whether the response includes archived time entries, when using the &#x60;startDate&#x60; and &#x60;endDate&#x60; parameters.  **Important**: this parameter _has no effect_ if you use the &#x60;modifiedStartDate&#x60; and &#x60;modifiedEndDate&#x60; parameters or the &#x60;businessDate&#x60; parameter to select time entries.  * Querying by modified date range _always_ returns archived time entries. * Querying by businessDate _never_ returns archived time entries.  This parameter is optional and the default value is &#x60;false&#x60;.  | [optional] 

### Return type

[**List[TimeEntry]**](TimeEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified time entries.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

