# toastapi.EmployeesApi

All URIs are relative to *https://ws-sandbox-api.eng.toasttab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employees_employee_id_delete**](EmployeesApi.md#employees_employee_id_delete) | **DELETE** /labor/v1/employees/{employeeId} | Delete an employee
[**employees_employee_id_external_id_post**](EmployeesApi.md#employees_employee_id_external_id_post) | **POST** /labor/v1/employees/{employeeId}/externalId | Add an external identifier
[**employees_employee_id_external_id_put**](EmployeesApi.md#employees_employee_id_external_id_put) | **PUT** /labor/v1/employees/{employeeId}/externalId | Add or replace an external identifier
[**employees_employee_id_get**](EmployeesApi.md#employees_employee_id_get) | **GET** /labor/v1/employees/{employeeId} | Get information about one employee
[**employees_employee_id_jobs_put**](EmployeesApi.md#employees_employee_id_jobs_put) | **PUT** /labor/v1/employees/{employeeId}/jobs | Replace a jobs list
[**employees_employee_id_patch**](EmployeesApi.md#employees_employee_id_patch) | **PATCH** /labor/v1/employees/{employeeId} | Update employee information
[**employees_employee_id_unarchive_put**](EmployeesApi.md#employees_employee_id_unarchive_put) | **PUT** /labor/v1/employees/{employeeId}/unarchive | Unarchive an employee
[**employees_employee_id_wage_overrides_put**](EmployeesApi.md#employees_employee_id_wage_overrides_put) | **PUT** /labor/v1/employees/{employeeId}/wageOverrides | Replace wage overrides
[**employees_get**](EmployeesApi.md#employees_get) | **GET** /labor/v1/employees | Get employees
[**employees_post**](EmployeesApi.md#employees_post) | **POST** /labor/v1/employees | Add an employee


# **employees_employee_id_delete**
> Employee employees_employee_id_delete(toast_restaurant_external_id, employee_id)

Delete an employee

Deletes a restaurant employee record by marking the record as 
deleted. A deleted employee cannot log in at the restaurant or 
open new time entries.

If you `GET` an employee record that has been deleted, its 
`deleted` value is `true` and its `deletedDate` value contains 
the date and time the record was deleted. 

If you delete an employee that has already been deleted then 
the result is successful (200) and no change is made.

The deleted record appears in the list of deleted employees for 
the restaurant in Toast Web. From the 
list of deleted employees, you can enable a deleted record so 
that the employee can use it again. Information about deleted 
employees remains available in reports.

You cannot delete employees who have open time entries (time 
entries that do not have an out date value).


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    employee_id = 'employee_id_example' # str | The Toast platform GUID or external identifier for the  employee to be deleted. 

    try:
        # Delete an employee
        api_response = await api_instance.employees_employee_id_delete(toast_restaurant_external_id, employee_id)
        print("The response of EmployeesApi->employees_employee_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_employee_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **employee_id** | **str**| The Toast platform GUID or external identifier for the  employee to be deleted.  | 

### Return type

[**Employee**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The employee has been deleted. Returns an &#x60;Employee&#x60; object  containing information about the deleted restaurant  employee.  |  -  |
**400** | The GUID or external identifier was malformed.  |  -  |
**404** | The GUID or external identifier does not match any employees at the current restaurant.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_employee_id_external_id_post**
> Employee employees_employee_id_external_id_post(employee_id, toast_restaurant_external_id, content_type, body)

Add an external identifier

Adds an external identifier for an existing employee. Include 
the string value of the new external identifier in the message 
body.

You cannot change an existing external identifier with another 
`POST` request; use `PUT` instead. The Toast platform uses this 
external identifier as one of the unique, persistent 
identifiers for an employee record.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | The Toast platform GUID of the employee record. 
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 
    body = 'body_example' # str | The JSON string value of the `externalId` for the employee  record. Wrap the value in double quotation marks to make it  valid JSON syntax. 

    try:
        # Add an external identifier
        api_response = await api_instance.employees_employee_id_external_id_post(employee_id, toast_restaurant_external_id, content_type, body)
        print("The response of EmployeesApi->employees_employee_id_external_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_employee_id_external_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The Toast platform GUID of the employee record.  | 
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 
 **body** | **str**| The JSON string value of the &#x60;externalId&#x60; for the employee  record. Wrap the value in double quotation marks to make it  valid JSON syntax.  | 

### Return type

[**Employee**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated employee record.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_employee_id_external_id_put**
> Employee employees_employee_id_external_id_put(employee_id, toast_restaurant_external_id, content_type, body)

Add or replace an external identifier

Adds or replaces the external identifier for an
existing employee. Include the string value of the new external
identifier in the message body.

The Toast platform uses this external identifier as one of the 
unique, persistent identifiers for an employee record. 
_Changing the external identifier for an existing employee 
might affect reporting and other Toast platform functions that 
select employees using the `externalId` value._


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | The Toast platform GUID of the employee record. 
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 
    body = 'body_example' # str | The JSON string value of the `externalId` for the employee  record. Wrap the value in double quotation marks to make it  valid JSON syntax. 

    try:
        # Add or replace an external identifier
        api_response = await api_instance.employees_employee_id_external_id_put(employee_id, toast_restaurant_external_id, content_type, body)
        print("The response of EmployeesApi->employees_employee_id_external_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_employee_id_external_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The Toast platform GUID of the employee record.  | 
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 
 **body** | **str**| The JSON string value of the &#x60;externalId&#x60; for the employee  record. Wrap the value in double quotation marks to make it  valid JSON syntax.  | 

### Return type

[**Employee**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated employee record.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_employee_id_get**
> Employee employees_employee_id_get(toast_restaurant_external_id, employee_id)

Get information about one employee

Returns an `Employee` object containing information about one 
restaurant employee.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    employee_id = 'employee_id_example' # str | The Toast platform GUID or external identifier for the  employee to be returned. 

    try:
        # Get information about one employee
        api_response = await api_instance.employees_employee_id_get(toast_restaurant_external_id, employee_id)
        print("The response of EmployeesApi->employees_employee_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_employee_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **employee_id** | **str**| The Toast platform GUID or external identifier for the  employee to be returned.  | 

### Return type

[**Employee**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the employee information.  |  -  |
**400** | The GUID or external identifier was malformed.  |  -  |
**404** | The GUID or external identifier does not match any  employees at the current restaurant.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_employee_id_jobs_put**
> Employee employees_employee_id_jobs_put(employee_id, toast_restaurant_external_id, content_type, body)

Replace a jobs list

Replaces the list of jobs for an employee. Include a JSON  
array of job identifiers in the message body.

If a job is defined at the restaurant group or subgroup level, 
this operation adds or removes that job for the the employee at 
_all restaurant locations_ in the group or subgroup.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | The Toast platform GUID of the employee record. 
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 
    body = 'body_example' # str | An array of JSON objects containing identifiers for jobs.  The identifiers can be either Toast platform GUIDs or  external identifiers. 

    try:
        # Replace a jobs list
        api_response = await api_instance.employees_employee_id_jobs_put(employee_id, toast_restaurant_external_id, content_type, body)
        print("The response of EmployeesApi->employees_employee_id_jobs_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_employee_id_jobs_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The Toast platform GUID of the employee record.  | 
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 
 **body** | **str**| An array of JSON objects containing identifiers for jobs.  The identifiers can be either Toast platform GUIDs or  external identifiers.  | 

### Return type

[**Employee**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated employee record.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_employee_id_patch**
> Employee employees_employee_id_patch(toast_restaurant_external_id, content_type, employee_id, body)

Update employee information

Updates the first name, chosen name, last name, external employee ID, and/or 
passcode of a restaurant employee. The `PATCH` operation cannot 
update any other employee information.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 
    employee_id = 'employee_id_example' # str | The Toast platform GUID or external identifier for the  employee to be returned. 
    body = 'body_example' # str | A JSON object containing the employee information that you  are updating. You can update an employee's:  * `firstName` - First name.  * `chosenName` - Chosen name.  * `lastName` - Last name.  * `externalEmployeeId` - External employee identifier.  * `passcode` - The passcode for access to Toast POS devices.  All values are optional. You must include at least one  value. Each value that you include must contain information  (not null). If you include the `passcode` value to update  an employee's passcode you must include the employee's  current passcode in the `currentPasscode` value. 

    try:
        # Update employee information
        api_response = await api_instance.employees_employee_id_patch(toast_restaurant_external_id, content_type, employee_id, body)
        print("The response of EmployeesApi->employees_employee_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_employee_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 
 **employee_id** | **str**| The Toast platform GUID or external identifier for the  employee to be returned.  | 
 **body** | **str**| A JSON object containing the employee information that you  are updating. You can update an employee&#39;s:  * &#x60;firstName&#x60; - First name.  * &#x60;chosenName&#x60; - Chosen name.  * &#x60;lastName&#x60; - Last name.  * &#x60;externalEmployeeId&#x60; - External employee identifier.  * &#x60;passcode&#x60; - The passcode for access to Toast POS devices.  All values are optional. You must include at least one  value. Each value that you include must contain information  (not null). If you include the &#x60;passcode&#x60; value to update  an employee&#39;s passcode you must include the employee&#39;s  current passcode in the &#x60;currentPasscode&#x60; value.  | 

### Return type

[**Employee**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated Toast platform employee record.  |  -  |
**400** | The Toast platform GUID or external identifier was  malformed, or the body of the request was malformed.  |  -  |
**404** | The Toast platform GUID or external identifier does not  match any employees at the current restaurant.  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_employee_id_unarchive_put**
> Employee employees_employee_id_unarchive_put(employee_id, toast_restaurant_external_id, content_type)

Unarchive an employee

Unarchives an employee record that was previously archived.

* Unarchived employees can sign into the Toast POS.
* Unarchived employees can sign in to Toast Web. 
* When you unarchive an employee, the employee has all 
  jobs that were previously assigned to them.
* If an employee had a swipe card for signing into the 
  Toast POS, the swipe card _is not_ re-associated with 
  the employee when you unarchive them.

If you unarchive an employee who will take a different 
role than the one they had when they were archived, you 
must update the employee's jobs list and verify that the 
employee should continue to sign into Toast Web.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | The Toast platform GUID of the employee record. 
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 

    try:
        # Unarchive an employee
        api_response = await api_instance.employees_employee_id_unarchive_put(employee_id, toast_restaurant_external_id, content_type)
        print("The response of EmployeesApi->employees_employee_id_unarchive_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_employee_id_unarchive_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The Toast platform GUID of the employee record.  | 
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 

### Return type

[**Employee**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated employee record.  |  -  |
**400** | Employee being unarchived is not currently archived.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_employee_id_wage_overrides_put**
> Employee employees_employee_id_wage_overrides_put(employee_id, toast_restaurant_external_id, content_type, body)

Replace wage overrides

Replaces the list of wage overrides for the jobs that are 
assigned to an employee. Include a JSON  array of 
`JobWageOverride` objects in the message body. Include the new 
wage for the employee in the `wage` value. Specify the wage in 
U.S. dollars.

You must include all existing wage overrides in the message 
body. Any wage overrides that are not present in the array are 
removed from the employee record.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | The Toast platform GUID of the employee record. 
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 
    body = 'body_example' # str | An array of JSON `JobWageOverride` objects. 

    try:
        # Replace wage overrides
        api_response = await api_instance.employees_employee_id_wage_overrides_put(employee_id, toast_restaurant_external_id, content_type, body)
        print("The response of EmployeesApi->employees_employee_id_wage_overrides_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_employee_id_wage_overrides_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The Toast platform GUID of the employee record.  | 
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 
 **body** | **str**| An array of JSON &#x60;JobWageOverride&#x60; objects.  | 

### Return type

[**Employee**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The wage overrides for the employee are replaced. Returns  the updated employee record.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_get**
> List[Employee] employees_get(toast_restaurant_external_id, employee_ids=employee_ids)

Get employees

Returns an array of `Employee` objects containing information 
about restaurant employees.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    employee_ids = 'employee_ids_example' # str | An optional identifier that filters return values for a  specific employee. The identifier can be a Toast platform  GUID or an external identifier. If present, the `employees`  resource will only return the employees you specify. You  can include multiple `employeeIds` query parameters  (maximum 100). If not present, the resource returns each  employee for the restaurant.  (optional)

    try:
        # Get employees
        api_response = await api_instance.employees_get(toast_restaurant_external_id, employee_ids=employee_ids)
        print("The response of EmployeesApi->employees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **employee_ids** | **str**| An optional identifier that filters return values for a  specific employee. The identifier can be a Toast platform  GUID or an external identifier. If present, the &#x60;employees&#x60;  resource will only return the employees you specify. You  can include multiple &#x60;employeeIds&#x60; query parameters  (maximum 100). If not present, the resource returns each  employee for the restaurant.  | [optional] 

### Return type

[**List[Employee]**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON objects for all employees in the restaurant  |  -  |
**500** | An unexpected internal error occurred. There is a  &#x60;requestId&#x60; attached to this error that can be referenced  by Toast support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_post**
> Employee employees_post(toast_restaurant_external_id, content_type, body)

Add an employee

Creates a restaurant employee record.


### Example

* OAuth Authentication (oauth2):

```python
import toastapi
from toastapi.models.employee import Employee
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
    api_instance = toastapi.EmployeesApi(api_client)
    toast_restaurant_external_id = 'toast_restaurant_external_id_example' # str | The Toast platform GUID of the restaurant that is the  context for this operation. 
    content_type = 'content_type_example' # str | The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  `application/json`. 
    body = 'body_example' # str | An `Employee` object containing information about the  employee, including the employee's name and email address. 

    try:
        # Add an employee
        api_response = await api_instance.employees_post(toast_restaurant_external_id, content_type, body)
        print("The response of EmployeesApi->employees_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toast_restaurant_external_id** | **str**| The Toast platform GUID of the restaurant that is the  context for this operation.  | 
 **content_type** | **str**| The Internet Assigned Numbers Authority (IANA) media type  of the message body data. The value must be  &#x60;application/json&#x60;.  | 
 **body** | **str**| An &#x60;Employee&#x60; object containing information about the  employee, including the employee&#39;s name and email address.  | 

### Return type

[**Employee**](Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the created employee. |  -  |
**400** | The request contains data that is not supported by the  current version of the API as described.  |  -  |
**415** | The request did not have \&quot;application/json\&quot; in the  Content-Type header.  |  -  |
**500** | An unexpected internal error occurred. There is a requestId  attached to this error that can be referenced by Toast  support.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

