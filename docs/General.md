# General

General information about a restaurant location. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The guest-facing name of the restaurant. For example, the &#x60;name&#x60; of a restaurant might be &#x60;Tommy&#39;s Burgers&#x60;.  | [optional] 
**location_name** | **str** | A name used externally to differentiate multiple locations, like Neighborhood, Square, City, or Hotel. | [optional] 
**location_code** | **str** | A code used internally to differentiate multiple locations, typically a 3 or 4 letter code. | [optional] 
**description** | **str** | A description of the restaurant, such as information about the atmosphere and food. | [optional] 
**time_zone** | **str** | The name of the restaurant&#39;s time zone in the &lt;a  href&#x3D;\&quot;https://www.iana.org/time-zones\&quot;&gt;IANA time zone  database&lt;/a&gt;. For example, &#x60;America/New_York&#x60;.  | [optional] 
**closeout_hour** | **int** | The hour of the day that separates one business day from the next, also known as the \&quot;business day cutoff time\&quot;. This is  in the time zone of the restaurant. The &#x60;closeoutHour&#x60; is set  to a value from 0-12 (midnight to noon) in the Business Day  Cutoff field in Toast Web.  | [optional] 
**management_group_guid** | **str** | The unique identifier of the restaurant group for the restaurant. | [optional] 
**currency_code** | **str** | The ISO-4217 currency code used in this restaurant | [optional] 
**first_business_date** | **int** | The first business date (yyyyMMdd) is the day a restaurant began using the Toast platform. The &#x60;firstBusinessDate&#x60; is also the first day on which time entries can be created for employees.  | [optional] 
**archived** | **bool** | Returns &#x60;true&#x60; if the restaurant has been archived from the Toast platform, otherwise returns &#x60;false&#x60;. A common reason for archiving a restaurant is if the restaurant was created in error.  | [optional] [default to False]

## Example

```python
from toastapi.models.general import General

# TODO update the JSON string below
json = "{}"
# create an instance of General from a JSON string
general_instance = General.from_json(json)
# print the JSON string representation of the object
print(General.to_json())

# convert the object into a dict
general_dict = general_instance.to_dict()
# create an instance of General from a dict
general_from_dict = General.from_dict(general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


