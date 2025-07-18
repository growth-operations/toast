# RestaurantV2

Information about the restaurant whose menu data has been retrieved. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restaurant_guid** | **str** | A unique identifier for this restaurant, assigned by the Toast POS system.  | [optional] 
**last_updated** | **str** | The most recent date and time that this menu&#39;s data was published. Use this value to determine if you need to refresh your menu data. The &#x60;lastUpdated&#x60; value uses the absolute timestamp format describe in the &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/api_dates_and_timestamps.html\&quot;&gt;Dates and timestamps&lt;/a&gt; section of the Toast Developer Guide.  | [optional] 
**restaurant_time_zone** | **str** | The name of the restaurant&#39;s time zone in the IANA time zone database https://www.iana.org/time-zones. For example, \&quot;America/New_York\&quot;.  | [optional] 
**menus** | [**List[MenuV2]**](MenuV2.md) | An array of &#x60;Menu&#x60; objects that represent the published menus used by this restaurant.  | [optional] 
**modifier_group_references** | [**Dict[str, ModifierGroupV2]**](ModifierGroupV2.md) | A map of &#x60;ModifierGroup&#x60; objects that define the modifier groups used by this restaurant. Each &#x60;ModifierGroup&#x60; object is presented as a key/value pair. A pair&#39;s key matches the &#x60;referenceId&#x60; of the object contained in the pair&#39;s value, as shown below: &#x60;&#x60;&#x60;   \&quot;modifierGroupReferences\&quot;: {     ...     \&quot;3\&quot;: {       \&quot;referenceId\&quot;: 3,       \&quot;name\&quot;: \&quot;Toppings\&quot;,       \&quot;guid\&quot;: \&quot;58b79986-f88f-411d-ba18-14b1e2441e9d\&quot;,         ...       },       ...       \&quot;modifierOptionReferences\&quot;: [         10,         11       ],       ...     },     ...   }, &#x60;&#x60;&#x60;  Other menu entities refer to modifier groups using their &#x60;referenceId&#x60;. Having a key that matches the &#x60;referenceId&#x60; allows you to locate the correct modifier group in the &#x60;modifierGroupReferences&#x60; map. For more information on the &#x60;referenceId&#x60; value, see the &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiUnderstandingGuidsEntityIdentifiersAndMultilocationIds_V2.html\&quot;&gt;Understanding GUIDs, referenceIds, and multilocationIds&lt;/a&gt; section of the Toast Developer Guide.  | [optional] 
**modifier_option_references** | [**Dict[str, ModifierOptionV2]**](ModifierOptionV2.md) | A map of &#x60;ModifierOption&#x60; objects that define the modifier options used by this restaurant. Each &#x60;ModifierOption&#x60; object is presented as a key/value pair. A pair&#39;s key matches the &#x60;referenceId&#x60; of the object contained in the pair&#39;s value, as shown below: &#x60;&#x60;&#x60; \&quot;modifierOptionReferences\&quot;: {   ...   \&quot;10\&quot;: {     \&quot;referenceId\&quot;: 10,     \&quot;name\&quot;: \&quot;Mushrooms\&quot;,     \&quot;guid\&quot;: \&quot;fa24fee9-76c4-40ba-ae3c-7dfccafdd8d3\&quot;,     ...   },   \&quot;11\&quot;: {     \&quot;referenceId\&quot;: 11,     \&quot;name\&quot;: \&quot;Onions\&quot;,     \&quot;guid\&quot;: \&quot;afee6be7-8280-4c69-a170-9fdf4c76bf7b\&quot;,     ...   },   ... } &#x60;&#x60;&#x60;  Other menu entities refer to modifier options using their &#x60;referenceId&#x60;. Having a key that matches the &#x60;referenceId&#x60; allows you to locate the correct modifier option in the &#x60;modifierOptionReferences&#x60; map. For more information on the &#x60;referenceId&#x60; value, see the &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiUnderstandingGuidsEntityIdentifiersAndMultilocationIds_V2.html\&quot;&gt;Understanding GUIDs, referenceIds, and multilocationIds&lt;/a&gt; section of the Toast Developer Guide.  | [optional] 
**pre_modifier_group_references** | [**Dict[str, PreModifierGroupV2]**](PreModifierGroupV2.md) | A map of &#x60;PreModifierGroup&#x60; objects that define the premodifier groups used by this restaurant. Each &#x60;PreModifierGroup&#x60; object is presented as a key/value pair. A pair&#39;s key matches the &#x60;referenceId&#x60; of the object contained in the pair&#39;s value, as shown below: &#x60;&#x60;&#x60; \&quot;preModifierGroupReferences\&quot;: {   \&quot;22\&quot;: {     \&quot;referenceId\&quot;: 22,     \&quot;guid\&quot;: \&quot;07a1a94d-6f7b-46d5-a916-a07fa16bb8e8\&quot;,     \&quot;name\&quot;: \&quot;PreModGroup\&quot;,     \&quot;preModifiers\&quot;: [       {         \&quot;guid\&quot;: \&quot;ad45e697-9356-468e-b7b4-1b23f4d4b8a5\&quot;,         \&quot;name\&quot;: \&quot;EXTRA\&quot;,         \&quot;fixedPrice\&quot;: 1.0,         \&quot;multiplicationFactor\&quot;: null,         \&quot;displayMode\&quot;: \&quot;PREFIX\&quot;       },       {         \&quot;guid\&quot;: \&quot;483dd4cf-acea-4373-ae76-5f7efd0d529d\&quot;,         \&quot;name\&quot;: \&quot;NO\&quot;,         \&quot;fixedPrice\&quot;: 0.0,         \&quot;multiplicationFactor\&quot;: null,         \&quot;displayMode\&quot;: \&quot;PREFIX\&quot;       }     ]   }, },             &#x60;&#x60;&#x60;  Other menu entities refer to premodifier groups using their &#x60;referenceId&#x60;. Having a key that matches the &#x60;referenceId&#x60; allows you to locate the correct premodifier group in the &#x60;preModifierGroupReferences&#x60; map. For more information on the &#x60;referenceId&#x60; value, see the &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiUnderstandingGuidsEntityIdentifiersAndMultilocationIds_V2.html\&quot;&gt;Understanding GUIDs, referenceIds, and multilocationIds&lt;/a&gt; section of the Toast Developer Guide.  | [optional] 

## Example

```python
from toastapi.models.restaurant_v2 import RestaurantV2

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantV2 from a JSON string
restaurant_v2_instance = RestaurantV2.from_json(json)
# print the JSON string representation of the object
print(RestaurantV2.to_json())

# convert the object into a dict
restaurant_v2_dict = restaurant_v2_instance.to_dict()
# create an instance of RestaurantV2 from a dict
restaurant_v2_from_dict = RestaurantV2.from_dict(restaurant_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


