# AlcoholV2

Information about whether this menu item or modifier contains alcohol and may require,  or benefit from, additional handling. For example, a delivery partner may need  to identify a menu item or modifier as containing alcohol to ensure that delivery drivers request identification before giving it to a customer. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contains_alcohol** | **str** | A string that indicates whether the menu item or modifier contains alcohol. Possible values  include:  * &#x60;YES&#x60;: The menu item or modifier contains alcohol. * &#x60;NO&#x60;: The menu item or modifier does not contain alcohol.       The &#x60;containsAlcohol&#x60; value may also be &#x60;null&#x60;. A &#x60;null&#x60; value indicates that the corresponding UI option in Toast Web has not been configured for this menu item or modifier.  | [optional] 

## Example

```python
from toastapi.models.alcohol_v2 import AlcoholV2

# TODO update the JSON string below
json = "{}"
# create an instance of AlcoholV2 from a JSON string
alcohol_v2_instance = AlcoholV2.from_json(json)
# print the JSON string representation of the object
print(AlcoholV2.to_json())

# convert the object into a dict
alcohol_v2_dict = alcohol_v2_instance.to_dict()
# create an instance of AlcoholV2 from a dict
alcohol_v2_from_dict = AlcoholV2.from_dict(alcohol_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


