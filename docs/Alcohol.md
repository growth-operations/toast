# Alcohol

Information about whether this menu item or modifier contains alcohol and may require,  or benefit from, additional handling. For example, a delivery partner may need  to identify a menu item or modifier as containing alcohol to ensure that delivery drivers request identification before giving it to a customer. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contains_alcohol** | **str** | A string that indicates whether the menu item or modifier contains alcohol. Possible values  include:  * &#x60;YES&#x60;: The menu item or modifier contains alcohol. * &#x60;NO&#x60;: The menu item or modifier does not contain alcohol.       The &#x60;containsAlcohol&#x60; value may also be &#x60;null&#x60;. A &#x60;null&#x60; value indicates that the corresponding UI option in Toast Web has not been configured for this menu item or modifier.  | [optional] 

## Example

```python
from toastapi.models.alcohol import Alcohol

# TODO update the JSON string below
json = "{}"
# create an instance of Alcohol from a JSON string
alcohol_instance = Alcohol.from_json(json)
# print the JSON string representation of the object
print(Alcohol.to_json())

# convert the object into a dict
alcohol_dict = alcohol_instance.to_dict()
# create an instance of Alcohol from a dict
alcohol_from_dict = Alcohol.from_dict(alcohol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


