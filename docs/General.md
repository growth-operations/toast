# General

General information about a restaurant location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The guest-facing name of the restaurant. | [optional] 
**location_name** | **str** | A name used externally to differentiate multiple locations. | [optional] 
**location_code** | **str** | A code used internally to differentiate multiple locations. | [optional] 
**description** | **str** | A description of the restaurant. | [optional] 
**time_zone** | **str** | The name of the restaurant&#39;s time zone in the IANA time zone database. | [optional] 
**closeout_hour** | **int** | The hour of the day that separates one business day from the next. | [optional] 
**management_group_guid** | **str** | The unique identifier of the restaurant group for the restaurant. | [optional] 
**currency_code** | **str** | The ISO-4217 currency code used in this restaurant. | [optional] 
**first_business_date** | **int** | The first business date (yyyyMMdd) the restaurant began using Toast. | [optional] 
**archived** | **bool** | Returns &#x60;true&#x60; if the restaurant has been archived from the Toast platform. | [optional] 

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


