# RestaurantPreModifierGroupReferences

A map of `PreModifierGroup` objects that define the premodifier groups used by this restaurant. Each `PreModifierGroup` object is presented as a key/value pair. A pair's key matches the `referenceId` of the object contained in the pair's value, as shown below: ... 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **int** |  | [optional] 

## Example

```python
from toastapi.models.restaurant_pre_modifier_group_references import RestaurantPreModifierGroupReferences

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantPreModifierGroupReferences from a JSON string
restaurant_pre_modifier_group_references_instance = RestaurantPreModifierGroupReferences.from_json(json)
# print the JSON string representation of the object
print(RestaurantPreModifierGroupReferences.to_json())

# convert the object into a dict
restaurant_pre_modifier_group_references_dict = restaurant_pre_modifier_group_references_instance.to_dict()
# create an instance of RestaurantPreModifierGroupReferences from a dict
restaurant_pre_modifier_group_references_from_dict = RestaurantPreModifierGroupReferences.from_dict(restaurant_pre_modifier_group_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


