# TipWithholding

Information about the way tip withholding is configured for a restaurant. Tip withholding is a percentage of employees' credit card tips and service charges that are paid to employees as a gratuity that is kept by a restaurant to cover credit card processing fees. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**enabled** | **bool** | Indicates whether a restaurant location withholds a percent of employees&#39; credit card tips.  * &#x60;true&#x60; - the location keeps a percent of employees&#39; credit card tips.  * &#x60;false&#x60; - the location does not keep a percent of employees&#39; credit card tips.  | [optional] 
**percentage** | **float** | The decimal percentage of credit card tips withheld. If tip withholding is not &#x60;enabled&#x60;, tips will not be withheld in the Toast platform regardless of this value.  | [optional] 

## Example

```python
from toastapi.models.tip_withholding import TipWithholding

# TODO update the JSON string below
json = "{}"
# create an instance of TipWithholding from a JSON string
tip_withholding_instance = TipWithholding.from_json(json)
# print the JSON string representation of the object
print(TipWithholding.to_json())

# convert the object into a dict
tip_withholding_dict = tip_withholding_instance.to_dict()
# create an instance of TipWithholding from a dict
tip_withholding_from_dict = TipWithholding.from_dict(tip_withholding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


