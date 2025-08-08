# PreModifier

Information about a pre-modifier configured for this restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for this pre-modifier, for example, \&quot;NO\&quot; or \&quot;EXTRA\&quot;.  | [optional] 
**guid** | **str** | A unique identifier for this pre-modifier group, assigned by the Toast POS system.  | [optional] 
**multi_location_id** | **str** | An identifier that is used to identify and consolidate menu entities that are versions of each other.  &#x60;multiLocationId&#x60; replaces &#x60;masterId&#x60;. &#x60;multiLocationId&#x60; and &#x60;masterId&#x60; always have the same value.  Menu entities can be versioned. Those versions can be assigned to specific restaurant locations, or groups of locations, in a management group. For example, you could have two versions of a burger, one for a Boston location and another for a New York City location. Versioned menu entities share the majority of, but not all of, their data. For example, the Boston version is called the Minuteman Burger and has pickles, while the New York City version is called the Empire Burger and does not.  You use the &#x60;multiLocationId&#x60; to identify menu entities that are versions of each other. To continue the example above, the Minuteman Burger in the JSON returned for the Boston location has the same &#x60;multilocationId&#x60; as the Empire Burger in the JSON returned for the New York City location. These matching &#x60;multlocationId&#x60; values indicate that the two items are related versions of the same item. In Toast reports, this allows a restaurant to track sales of the burger across both locations.  | [optional] 
**fixed_price** | **float** | An optional fixed price for this pre-modifier. The fixed price is added to the cost of the modifier option that the pre-modifier is applied to.  A PreModifier object has two optional values, &#x60;fixedPrice&#x60; and &#x60;multiplicationFactor&#x60;, that both alter the price of a modifier option when the pre-modifier is applied to it. However, these values cannot be used at the same time. If you specify a &#x60;fixedPrice&#x60; value for a premodifier, then &#x60;multiplicationFactor&#x60; is null. If you specify a &#x60;multiplicationFactor&#x60; for a pre-modifier, then &#x60;fixedPrice&#x60; is null. If you choose not to assign either a fixed price or a multiplication factor to a pre-modifier, then the &#x60;fixedPrice&#x60; value is 0 and the &#x60;multiplicationFactor&#x60; is null.  | [optional] 
**multiplication_factor** | **float** | An optional number that specifies how much the cost of a modifier option is multiplied by when this pre-modifier is applied to it. For example, an EXTRA pre-modifier option could specify a &#x60;multiplicationFactor&#x60; of 1.5 to indicate that adding extra cheese to a menu item costs one and a half times the regular price of the cheese modifier option.  A PreModifier object has two optional values, &#x60;fixedPrice&#x60; and &#x60;multiplicationFactor&#x60;, that both alter the price of a modifier option when the pre-modifier is applied to it. However, these values cannot be used at the same time. If you specify a &#x60;fixedPrice&#x60; value for a premodifier, then &#x60;multiplicationFactor&#x60; is null. If you specify a &#x60;multiplicationFactor&#x60; for a premodifier, then &#x60;fixedPrice&#x60; is null. If you choose not to assign either a fixed price or a multiplication factor to a pre-modifier, then the &#x60;fixedPrice&#x60; value is 0 and the &#x60;multiplicationFactor&#x60; is null.  | [optional] 
**display_mode** | **str** | The display mode for this pre-modifier option.  | [optional] 

## Example

```python
from toastapi.models.pre_modifier import PreModifier

# TODO update the JSON string below
json = "{}"
# create an instance of PreModifier from a JSON string
pre_modifier_instance = PreModifier.from_json(json)
# print the JSON string representation of the object
print(PreModifier.to_json())

# convert the object into a dict
pre_modifier_dict = pre_modifier_instance.to_dict()
# create an instance of PreModifier from a dict
pre_modifier_from_dict = PreModifier.from_dict(pre_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


