# ServiceCharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**name** | **str** | The name of this service charge. | [optional] 
**amount_type** | **str** | The type of service charge. | [optional] 
**amount** | **float** | Amount in USD to be applied for &#x60;FIXED&#x60; type service charges. | [optional] 
**percent** | **float** | Percent fee to be applied for &#x60;PERCENT&#x60; type service charges, based on pre-discount check amount. Must be a number between 0 and 100.  | [optional] 
**criteria** | [**ServiceChargeCriteria**](ServiceChargeCriteria.md) |  | [optional] 
**gratuity** | **bool** | True if the service charge is a gratuity and is assigned to the owner of the check. | [optional] 
**taxable** | **bool** | True if tax should be applied to the service charge. | [optional] 
**applicable_taxes** | [**List[TaxRate]**](TaxRate.md) | A reference to the taxes applied to the service charge, if the service charge is taxable. | [optional] 
**service_charge_calculation** | **str** | Defines whether or not the service charge is applied before (PRE) or after (POST) discounts. This field is null for non-percent service charges. | [optional] 
**destination** | **str** | Final recipient of the funds from this service charge.  * &#x60;RESTAURANT&#x60; - The business owner of the restaurant receives the service charge funds. * &#x60;SERVER&#x60; - Restaurant employees receive the service charge funds e.g. gratuity. * &#x60;TOAST&#x60; - Toast receives the service charge funds. * &#x60;THIRD_PARTY&#x60; - A third party receives the service charge funds e.g. fundraising funds go to charity.  | [optional] 

## Example

```python
from toastapi.models.service_charge import ServiceCharge

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCharge from a JSON string
service_charge_instance = ServiceCharge.from_json(json)
# print the JSON string representation of the object
print(ServiceCharge.to_json())

# convert the object into a dict
service_charge_dict = service_charge_instance.to_dict()
# create an instance of ServiceCharge from a dict
service_charge_from_dict = ServiceCharge.from_dict(service_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


