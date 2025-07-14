# RestaurantModifierOptionReferences

A map of `ModifierOption` objects that define the modifier options used by this restaurant. Each `ModifierOption` object is presented as a key/value pair. A pair's key matches the `referenceId` of the object contained in the pair's value, as shown below: ... 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **int** |  | [optional] 

## Example

```python
from toastapi.models.restaurant_modifier_option_references import RestaurantModifierOptionReferences

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantModifierOptionReferences from a JSON string
restaurant_modifier_option_references_instance = RestaurantModifierOptionReferences.from_json(json)
# print the JSON string representation of the object
print(RestaurantModifierOptionReferences.to_json())

# convert the object into a dict
restaurant_modifier_option_references_dict = restaurant_modifier_option_references_instance.to_dict()
# create an instance of RestaurantModifierOptionReferences from a dict
restaurant_modifier_option_references_from_dict = RestaurantModifierOptionReferences.from_dict(restaurant_modifier_option_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


