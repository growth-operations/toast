# Discount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**name** | **str** | The human-readable name of the discount. | [optional] 
**active** | **bool** | Indicates whether the discount is available and can be applied by restaurant employees.  | [optional] 
**type** | **str** | * &#x60;PERCENT&#x60; - the discount reduces the price by a preconfigured percent. * &#x60;FIXED&#x60; - the discount reduces the price by a preconfigured currency amount. * &#x60;OPEN_PERCENT&#x60; - the discount reduces the price by a percent entered by a restaurant employee. * &#x60;OPEN_FIXED&#x60; - the discount reduces the price by a currency amount entered by a restaurant employee. * &#x60;BOGO&#x60; - a buy one get one (BOGO) discount. * &#x60;FIXED_TOTAL&#x60; - a combo discount that reduces the price of all eligible items to a preconfigured currency amount.  | [optional] 
**percentage** | **float** | Percent discount applied when the &#x60;amountType&#x60; is &#x60;PERCENT&#x60;. This value will be greater than 0 and at most 100.  | [optional] 
**amount** | **float** | The currency amount of the discount when the &#x60;amountType&#x60; is &#x60;FIXED&#x60;. This value will be greater than 0.  | [optional] 
**selection_type** | **str** | * &#x60;CHECK&#x60; - the discount can be applied to a check. * &#x60;BOGO&#x60; - a buy one get one (BOGO) discount. * &#x60;ITEM&#x60; - the discount can be applied to an item selection in a check.  | [optional] 
**non_exclusive** | **bool** | Indicates whether you can apply the discount with other discounts. This value is always &#x60;false&#x60; for item and combo discounts. Set this value for check and BOGO discounts by selecting **Allow with other discounts** in the **Discounts Rules** section of the discounts configuration page of Toast Web.  | [optional] 
**item_picking_priority** | **str** | Indicates which menu item selections are discounted when you apply a BOGO discount. An item that is discounted by a BOGO discount is a \&quot;get\&quot; item.  * &#x60;FIRST&#x60; - the BOGO discount applies to the first matching item selection in the check or the discount is not a BOGO discount. The &#x60;itemPickingPriority&#x60; is always &#x60;FIRST&#x60; for discounts that are not BOGO discounts.  * &#x60;LEAST_EXPENSIVE&#x60; - the BOGO discount applies to the least expensive matching item selection in the check.  * &#x60;MOST_EXPENSIVE&#x60; - the BOGO discount applies to the most expensive matching item selection in the check.  | [optional] 

## Example

```python
from toastapi.models.discount import Discount

# TODO update the JSON string below
json = "{}"
# create an instance of Discount from a JSON string
discount_instance = Discount.from_json(json)
# print the JSON string representation of the object
print(Discount.to_json())

# convert the object into a dict
discount_dict = discount_instance.to_dict()
# create an instance of Discount from a dict
discount_from_dict = Discount.from_dict(discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


