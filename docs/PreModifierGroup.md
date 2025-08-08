# PreModifierGroup

Information about a pre-modifier group configured for this restaurant, including an array of pre-modifiers contained in the group. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this pre-modifier group, for example, \&quot;Sandwich Pre-mods\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this pre-modifier group, assigned by the Toast POS system.  | [optional] 
**multi_location_id** | **str** | An identifier that is used to identify and consolidate menu entities that are versions of each other.  &#x60;multiLocationId&#x60; replaces &#x60;masterId&#x60;. &#x60;multiLocationId&#x60; and &#x60;masterId&#x60; always have the same value.  Menu entities can be versioned. Those versions can be assigned to specific restaurant locations, or groups of locations, in a management group. For example, you could have two versions of a burger, one for a Boston location and another for a New York City location. Versioned menu entities share the majority of, but not all of, their data. For example, the Boston version is called the Minuteman Burger and has pickles, while the New York City version is called the Empire Burger and does not.  You use the &#x60;multiLocationId&#x60; to identify menu entities that are versions of each other. To continue the example above, the Minuteman Burger in the JSON returned for the Boston location has the same &#x60;multilocationId&#x60; as the Empire Burger in the JSON returned for the New York City location. These matching &#x60;multlocationId&#x60; values indicate that the two items are related versions of the same item. In Toast reports, this allows a restaurant to track sales of the burger across both locations.  | [optional] 
**pre_modifiers** | [**List[PreModifier]**](PreModifier.md) | An array of &#x60;PreModifier&#x60; objects that are contained in this pre-modifier group. Pre-modifiers alter the display of modifier options on receipts and tickets to satisfy guest requests such as EXTRA or ON THE SIDE for modifier options. Pre-modifiers can also be configured to modify the cost of the modifier options they are applied to, for example, by charging more for an EXTRA serving of a modifier option.  | [optional] 

## Example

```python
from toastapi.models.pre_modifier_group import PreModifierGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PreModifierGroup from a JSON string
pre_modifier_group_instance = PreModifierGroup.from_json(json)
# print the JSON string representation of the object
print(PreModifierGroup.to_json())

# convert the object into a dict
pre_modifier_group_dict = pre_modifier_group_instance.to_dict()
# create an instance of PreModifierGroup from a dict
pre_modifier_group_from_dict = PreModifierGroup.from_dict(pre_modifier_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


