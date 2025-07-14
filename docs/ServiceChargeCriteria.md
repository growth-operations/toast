# ServiceChargeCriteria

Describes thresholds for when a service charge should be applied to a check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_check_amount** | **float** | The service charge is only applicable if the pre-discount check is at least this amount. | [optional] 
**delivery** | **bool** | True if the service charge is only applicable for deliveries. | [optional] 
**max_check_amount** | **float** | The service charge is waived if the pre-discount check amount is more than this amount. A &#x60;null&#x60; value means this criteria is inapplicable. | [optional] 
**min_delivery_distance** | **float** | The service charge is only applicable to deliveries that are at least this distance. A &#x60;null&#x60; value means this criteria is inapplicable. | [optional] 
**takeout** | **bool** | Indicates whether the service charge is automatically applied to orders that have the takeout dining option behavior. | [optional] 
**dine_in** | **bool** | Indicates whether the service charge is applied to orders that have the dine-in dining option behavior. | [optional] 

## Example

```python
from toastapi.models.service_charge_criteria import ServiceChargeCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceChargeCriteria from a JSON string
service_charge_criteria_instance = ServiceChargeCriteria.from_json(json)
# print the JSON string representation of the object
print(ServiceChargeCriteria.to_json())

# convert the object into a dict
service_charge_criteria_dict = service_charge_criteria_instance.to_dict()
# create an instance of ServiceChargeCriteria from a dict
service_charge_criteria_from_dict = ServiceChargeCriteria.from_dict(service_charge_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


