# ApplicableDiscount

A wrapper object that contains information about a discount that you can apply to an order, and which checks or menu item selections you can apply it to. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | [**ToastReference**](.md) |  | 
**applicable_checks** | [**List[ExternalReference]**](ExternalReference.md) | If the discount is applicable to a check, this value holds an array of &#x60;ExternalReference&#x60; objects containing the identifiers of the checks.  | [optional] 
**applicable_selections** | [**List[ExternalReference]**](ExternalReference.md) | If the discount is applicable to a menu item selection, this value holds an array of &#x60;ExternalReference&#x60; objects containing the identifiers of the menu items.  | [optional] 

## Example

```python
from toastapi.models.applicable_discount import ApplicableDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicableDiscount from a JSON string
applicable_discount_instance = ApplicableDiscount.from_json(json)
# print the JSON string representation of the object
print(ApplicableDiscount.to_json())

# convert the object into a dict
applicable_discount_dict = applicable_discount_instance.to_dict()
# create an instance of ApplicableDiscount from a dict
applicable_discount_from_dict = ApplicableDiscount.from_dict(applicable_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


