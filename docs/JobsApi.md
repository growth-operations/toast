# toastapi.JobsApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_external_identifier_to_job**](JobsApi.md#add_external_identifier_to_job) | **POST** /labor/v1/jobs/{jobId}/externalId | Add an external identifier
[**add_or_replace_external_identifier_to_job**](JobsApi.md#add_or_replace_external_identifier_to_job) | **PUT** /labor/v1/jobs/{jobId}/externalId | Add or replace an external identifier
[**get_job_by_id**](JobsApi.md#get_job_by_id) | **GET** /labor/v1/jobs/{jobId} | Get one job
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /labor/v1/jobs | Get jobs


# **add_external_identifier_to_job**
> Job add_external_identifier_to_job(job_id, toast_restaurant_external_id, content_type, body)

Add an external identifier

Adds an external identifier for an existing job. Include the 
string value of the new external identifier in the message 
body.

You cannot change an existing external identifier with another 
`POST` request. The Toast platform uses this external 
identifier as one of the unique, persistent identifiers for a 
job record.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.job import Job
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
    api_instance = toastapi.JobsApi(api_client)
    job_id = 'job_id_example' # str | The Toast platform GUID or external identifier of the job  record. 
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 
    body = 'body_example' # str | The JSON string value of the `externalId` for the job  record. Wrap the value in double quotation marks to make it  valid JSON syntax. 

    try:
        # Add an external identifier
        api_response = await api_instance.add_external_identifier_to_job(job_id, toast_restaurant_external_id, content_type, body)
        print("The response of JobsApi->add_external_identifier_to_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->add_external_identifier_to_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The Toast platform GUID or external identifier of the job  record.  | 
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 
 **body** | **str**| The JSON string value of the &#x60;externalId&#x60; for the job  record. Wrap the value in double quotation marks to make it  valid JSON syntax.  | 

### Return type

[**Job**](Job.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated job record.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_or_replace_external_identifier_to_job**
> Job add_or_replace_external_identifier_to_job(job_id, toast_restaurant_external_id, content_type, body)

Add or replace an external identifier

Adds or replaces the external identifier for an existing job. 
Include the string value of the new external identifier in the 
message body.

The Toast platform uses this external identifier as one of the 
unique, persistent identifiers for a job record. _Changing the 
external identifier for an existing job might affect reporting 
and other Toast platform functions that select jobs using the 
`externalId` value._


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.job import Job
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
    api_instance = toastapi.JobsApi(api_client)
    job_id = 'job_id_example' # str | The Toast platform GUID or external identifier of the job  record. 
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 
    body = 'body_example' # str | The JSON string value of the `externalId` for the job  record. Wrap the value in double quotation marks to make it  valid JSON syntax. 

    try:
        # Add or replace an external identifier
        api_response = await api_instance.add_or_replace_external_identifier_to_job(job_id, toast_restaurant_external_id, content_type, body)
        print("The response of JobsApi->add_or_replace_external_identifier_to_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->add_or_replace_external_identifier_to_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The Toast platform GUID or external identifier of the job  record.  | 
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 
 **body** | **str**| The JSON string value of the &#x60;externalId&#x60; for the job  record. Wrap the value in double quotation marks to make it  valid JSON syntax.  | 

### Return type

[**Job**](Job.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated job record.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_by_id**
> Job get_job_by_id(toast_restaurant_external_id, job_id)

Get one job

Returns a `Job` object containing information about one 
employee job at a restaurant.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.job import Job
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
    api_instance = toastapi.JobsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    job_id = 'job_id_example' # str | The Toast platform GUID or an external identifier for the  job. 

    try:
        # Get one job
        api_response = await api_instance.get_job_by_id(toast_restaurant_external_id, job_id)
        print("The response of JobsApi->get_job_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **job_id** | **str**| The Toast platform GUID or an external identifier for the  job.  | 

### Return type

[**Job**](Job.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified job.  |  -  |
**400** | The Toast platform GUID or external identifier was  malformed.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> List[Job] list_jobs(toast_restaurant_external_id, job_ids=job_ids)

Get jobs

Returns an array of `Job` objects containing information about 
the employee jobs configured at a restaurant.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.job import Job
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
    api_instance = toastapi.JobsApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    job_ids = ['job_ids_example'] # List[str] | An optional array of one or more job identifiers, either  the Toast platform GUID or an external identifier assigned  by the client. 100 max. If not provided, all jobs known to  the Toast platform for this restaurant will be returned.  (optional)

    try:
        # Get jobs
        api_response = await api_instance.list_jobs(toast_restaurant_external_id, job_ids=job_ids)
        print("The response of JobsApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **job_ids** | [**List[str]**](str.md)| An optional array of one or more job identifiers, either  the Toast platform GUID or an external identifier assigned  by the client. 100 max. If not provided, all jobs known to  the Toast platform for this restaurant will be returned.  | [optional] 

### Return type

[**List[Job]**](Job.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified jobs.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

