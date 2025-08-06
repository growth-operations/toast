# Selection

A `Selection` object can represent either a primary item (for example, `Check.selections`) or a modifier (`Selection.modifiers`) selection. Quantity defaults to `1`.  For a `POST` operation, all selections must have valid `item` and `itemGroup` fields. The `item` and `itemGroup` values can be `null` for `GET` requests. For example, they are `null` for gift cards and on special requests.  To specify a modifier selection, add it to the `modifiers` list of another selection. Each modifier selection must have its `optionGroup` field set correctly, because a `MenuItem` can be included in multiple `MenuOptionGroups`, potentially with different prices or sizing. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**item** | [**ConfigReference**](ConfigReference.md) |  | 
**item_group** | [**ConfigReference**](ConfigReference.md) |  | [optional] 
**option_group** | [**ConfigReference**](ConfigReference.md) |  | [optional] 
**pre_modifier** | [**ConfigReference**](ConfigReference.md) |  | [optional] 
**quantity** | **float** | Quantity ordered. For items sold by weight, a decimal number. For discrete items, a counting number. | 
**seat_number** | **int** | Indicates which guest seat at a restaurant table ordered a menu item selection. Restaurant employees can choose the seat number when they add a menu item to a guest check.  * A positive integer value indicates the seat number for   the menu item.  * &#x60;0&#x60; - Indicates that the menu item is shared by   multiple guests.  * &#x60;-1&#x60; - Indicates that the restaurant employee did not   select a seat for the menu item.  Response only.  | [optional] 
**unit_of_measure** | **str** | The unit of measure required for weighing the item.  The default is &#x60;NONE&#x60;, which means that the item is not meant to be weighed.  | [optional] 
**selection_type** | **str** | Specifies whether this selection is a special request or other off-menu sale.  If &#x60;null&#x60; or &#x60;NONE&#x60;, describes a normal modifier or item selection.  &#x60;TOAST_CARD_SELL&#x60; and &#x60;TOAST_CARD_RELOAD&#x60; are currently response-only.  | [optional] 
**sales_category** | [**ConfigReference**](ConfigReference.md) |  | [optional] 
**applied_discounts** | [**List[AppliedDiscount]**](AppliedDiscount.md) | The itemized discounts that are applied to this item. Response only. | [optional] 
**deferred** | **bool** | Whether this selection is a deferred revenue transaction, such as a gift card sale. | [optional] 
**pre_discount_price** | **float** | Gross sale price for this selection. Excludes tax. Response only. | [optional] 
**price** | **float** | Net price for this selection. The final price of the item after considering discounts (including discounts at the check level), quantity adjustments, and modifier prices at the time the item was selected for purchase. Response only. | [optional] 
**tax** | **float** | The total tax amount for this selection. Response only. | [optional] 
**voided** | **bool** | Set to &#x60;true&#x60; if this selection is voided. Response only. | [optional] 
**void_date** | **datetime** | The date on which this selection was voided. Response only. | [optional] 
**void_business_date** | **int** | The business date (yyyyMMdd) on which this selection was voided. Response only. | [optional] 
**void_reason** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**refund_details** | [**RefundDetails**](RefundDetails.md) |  | [optional] 
**display_name** | **str** | The display name of the selection.  Can be used to set a special request value.  Otherwise, it is generated from this selection&#39;s item property.  | [optional] 
**created_date** | **datetime** | The date on which this selection was created. If not specified, defaults to the current time. | [optional] 
**modified_date** | **datetime** | The date on which this selection was last modified. If not specified, defaults to the current time. | [optional] 
**modifiers** | [**List[Selection]**](Selection.md) | A list of modifiers that apply to this selection. | [optional] 
**fulfillment_status** | **str** | Indicates the stage of the preparation workflow that the menu item selection is in.  The &#x60;fulfillmentStatus&#x60; of a menu item selection changes as restaurant employees move the item through the functions of the Toast POS, for example order entry and the kitchen display system (KDS). Response only.  Valid values:  * &#x60;NEW&#x60; - The menu item selection was added to a   check but is not yet sent to the KDS for   preparation.  * &#x60;HOLD&#x60; - A restaurant employee paused the menu   item selection so that it does not appear in the   KDS for preparation.  * &#x60;SENT&#x60; - The menu item selection was fired and   appears in the KDS for preparation.  * &#x60;READY&#x60; - Preparation is complete. The menu item   selection is fulfilled and no longer appears in   the KDS. If your restaurant does not use the Toast platform   KDS, then order items do not reach the &#x60;READY&#x60;   status.  | [optional] [default to 'NEW']
**tax_inclusion** | **str** | Indicates whether the menu item price includes one or more tax amounts. If the menu item is a modifier for another menu item selection, it always inherits the tax inclusion behavior of the menu item that it applies to.  Valid values: * &#x60;INCLUDED&#x60; - The menu item price includes one or more tax amounts. * &#x60;NOT_INCLUDED&#x60; - The menu item price does not include any tax   amounts. * &#x60;INHERITED&#x60; - The menu item is a modifier for another menu item   selection in the check. The &#x60;taxInclusion&#x60; value of the parent menu   item selection applies to the modifier. If a menu item selection   *that is not a modifier* inherits tax inclusion behavior from a   menu or menu group, the &#x60;taxInclusion&#x60; value is either   &#x60;INCLUDED&#x60; or &#x60;NOT_INCLUDED&#x60;.  | [optional] 
**applied_taxes** | [**List[AppliedTaxRate]**](AppliedTaxRate.md) | An array of &#x60;AppliedTaxRate&#x60; objects that contain information about tax payments made for the selection. Response only. | [optional] 
**dining_option** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**open_price_amount** | **float** | A non-negative currency amount that sets the price of a menu item that is configured to use the *Open Price* pricing strategy. If you do not supply an &#x60;openPriceAmount&#x60; value for an open price menu item, the orders API sets the price to 0.00.  If a menu item is configured to use tax-inclusive pricing, the orders API calculates the base price and tax amount based on the open price that you specify. _The open-price amount includes both the base-price and inclusive tax amount._  &#x60;POST&#x60; only. The &#x60;openPriceAmount&#x60; value is not present in orders API return data. It is used to populate &#x60;receiptLinePrice&#x60;.  | [optional] 
**receipt_line_price** | **float** | The price of the menu item selection without any quantity, taxes,  discounts, and modifier adjustments. If the menu item has taxes included, the &#x60;receiptLinePrice&#x60; value shows the original price, including taxes.  For example, if the menu item selection is for two orders of fries,  &#x60;receiptLinePrice&#x60; is the price of one order of fries. If a menu item selection  is for three large drinks, receiptLinePrice is the price of one large drink.  Populated based on the menu configuration, or using the value provided in  &#x60;externalPriceAmount&#x60; or &#x60;openPriceAmount&#x60;.  | [optional] 
**option_group_pricing_mode** | **str** | Information about how the modifier group affects the pricing of its parent item. | [optional] 
**external_price_amount** | **float** | The menu item price that was calculated by the marketplace facilitator organization that created the order.  &#x60;POST&#x60; only. The orders API does not include the &#x60;externalPriceAmount&#x60; value in return data. It is used to populate &#x60;receiptLinePrice&#x60;.  **Note**: you can only include this information if your Toast API client is associated with a designated marketplace facilitator organization. Most Toast API clients do not create marketplace facilitator orders.  | [optional] 
**split_origin** | [**ToastReference**](ToastReference.md) |  | [optional] 

## Example

```python
from toastapi.models.selection import Selection

# TODO update the JSON string below
json = "{}"
# create an instance of Selection from a JSON string
selection_instance = Selection.from_json(json)
# print the JSON string representation of the object
print(Selection.to_json())

# convert the object into a dict
selection_dict = selection_instance.to_dict()
# create an instance of Selection from a dict
selection_from_dict = Selection.from_dict(selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


