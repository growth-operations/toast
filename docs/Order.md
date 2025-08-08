# Order

A Toast platform order is composed of one or more checks. Each check has  one or more menu item selections. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**opened_date** | **datetime** | The business date of the order.  For dine-in and as soon as possible (ASAP) orders, &#x60;openedDate&#x60; should match &#x60;createdDate&#x60;.  For scheduled orders, &#x60;openedDate&#x60; should match &#x60;promisedDate&#x60;.  If you do not provide a value for  &#x60;openedDate&#x60; value when you &#x60;POST&#x60; a new order, the business date of the order is set to the restaurant business day that corresponds to the current date and time.  The business date of an order is affected by the business date cutoff time for a restaurant, which is available from the restaurants API in the &#x60;closeoutHour&#x60; property.  | [optional] 
**modified_date** | **datetime** | The most recent date that the order, or a check or menu item selection in the order, was modified. | [optional] 
**promised_date** | **datetime** | For scheduled orders, the date and time that the order is scheduled to be fulfilled.  For dine-in and as soon as possible (ASAP) orders, &#x60;promisedDate&#x60; is &#x60;null&#x60;.  | [optional] 
**channel_guid** | **str** | Reserved for future use.  | [optional] 
**dining_option** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**checks** | [**List[Check]**](Check.md) | The checks for this order. Most orders have one check.  If the check is split, then there are multiple checks.  | 
**table** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**service_area** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**restaurant_service** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**revenue_center** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**source** | **str** | Indicates the way that the order was placed.  Valid values:  * &#x60;In Store&#x60; * &#x60;Online&#x60; * &#x60;Order-and-Pay-at-Table&#x60; * &#x60;API&#x60; * &#x60;Kiosk&#x60; * &#x60;Caller Id&#x60; * &#x60;Google&#x60; * &#x60;Invoice&#x60; * &#x60;Toast Pickup App&#x60; * &#x60;Toast Local&#x60; * &#x60;Branded Online Ordering&#x60; * &#x60;Catering&#x60; * &#x60;Catering Online Ordering&#x60; * &#x60;Toast Tables&#x60; * &#x60;eCommerce Online ordering&#x60; * &#x60;Branded Mobile App * &#x60;Grubhub&#x60; (deprecated)  Response only.  | [optional] 
**duration** | **int** | The number of seconds between creation and payment. Response only. | [optional] 
**delivery_info** | [**DeliveryInfo**](DeliveryInfo.md) |  | [optional] 
**required_prep_time** | **str** | The amount of time that it will take to prepare the order. This value overrides the  default &#x60;deliveryPrepTime&#x60; or &#x60;takeoutPrepTime&#x60; that normally controls auto-firing for scheduled orders.  You can use &#x60;requiredPrepTime&#x60; to handle atypical orders that will take more time than usual for a restaurant to prepare.  Express the required preparation time in ISO-8601 duration format. Must be greater than zero and be an  increment of five minutes. For example, the value \&quot;PT15M\&quot; sets the required preparation time for the order to 15 minutes.  | [optional] 
**estimated_fulfillment_date** | **datetime** | The date and time that the order is expected to be ready for pickup or to be delivered.  This value is only set when the order dining option uses the &#x60;DELIVERY&#x60; or &#x60;TAKE_OUT&#x60; dining behavior. For other dining options, the value is &#x60;null&#x60;.  Response only.  | [optional] 
**number_of_guests** | **int** | The number of restaurant guests that are associated with the order. For example, for a dine-in order, this might be the number of guests at a table.  | [optional] 
**voided** | **bool** | Set to &#x60;true&#x60; if this order was voided. Response only. | [optional] 
**void_date** | **datetime** | The date on which this order was voided. Response only. | [optional] 
**void_business_date** | **int** | The business date (yyyyMMdd) on which this order was voided. Response only. | [optional] 
**paid_date** | **datetime** | The most recent date on which this order received payment. If not specified when &#x60;POST&#x60;ing, it is set to the current system time. | [optional] 
**closed_date** | **datetime** | The most recent date on which the order payment status changed to &#x60;CLOSED&#x60;.  This status is not returned for the order. The order is simply &#x60;CLOSED&#x60; when all of the checks on the order are &#x60;CLOSED&#x60;.  | [optional] 
**deleted_date** | **datetime** | The date and time when the order was deleted.  The &#x60;deletedDate&#x60; value only applies when the &#x60;deleted&#x60; value is &#x60;true&#x60;.  If &#x60;deleted&#x60; is &#x60;false&#x60;, the value of &#x60;deletedDate&#x60; is the UNIX epoch, &#x60;1970-01-01T00:00:00.000+0000&#x60;.  | [optional] 
**deleted** | **bool** | Set to &#x60;true&#x60; if this order is deleted. Response only.  For example, if you combine a check into another order, the original order for the check is deleted.  | [optional] 
**business_date** | **int** | The business date (yyyyMMdd) on which the order was fulfilled. Response only. | [optional] 
**applied_packaging_info** | [**AppliedPackagingInfo**](AppliedPackagingInfo.md) |  | [optional] 
**approval_status** | **str** | The current state of the order in the restaurant order fulfillment process. For example, the &#x60;approvalStatus&#x60; can indicate that an order is waiting for a restaurant employee to approve it or that the order is in a restaurant kitchen being fulfilled. Response only.  Valid values:  * &#x60;NEEDS_APPROVAL&#x60; - The order is created but will not be fulfilled by the restaurant until an employee approves it.  * &#x60;APPROVED&#x60; - The order is being fulfilled by the restaurant or it was fulfilled in the past. Orders remain in this state indefinitely after they are fulfilled.  * &#x60;FUTURE&#x60; - The order is expected to be fulfilled by the restaurant at a future date and time. Restaurant employees will receive information about the order at the date and time that it is ready to be fulfilled.  * &#x60;NOT_APPROVED&#x60; - Restaurant employees received information about the order but did not approve it for fulfillment. An order enters this state after a period of time passes without a restaurant employee approving it.  | [optional] 
**created_device** | [**Device**](Device.md) |  | [optional] 
**created_in_test_mode** | **bool** | Indicates whether the order was created while the restaurant was in test mode.  For more information, see [this _Toast Central_ article](https://central.toasttab.com/s/article/Test-Mode-Enable-and-Disable-1492802389999)  | [optional] 
**curbside_pickup_info** | [**CurbsidePickupInfo**](CurbsidePickupInfo.md) |  | [optional] 
**delivery_service_info** | [**DeliveryServiceInfo**](DeliveryServiceInfo.md) |  | [optional] 
**display_number** | **str** | Response only. Generally starts at one each day and counts up. Not guaranteed to be unique, can be empty if unset. | [optional] 
**excess_food** | **bool** | Indicates whether the order was created to track excess food (for example, food waste) rather than a  standard guest order. Response only.  For more information on the differences between guest orders and excess food orders, see  &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/apiDailyOrderForTrackingExcessFood.html\&quot;&gt;Daily order for tracking excess food&lt;/a&gt;.  | [optional] 
**guest_order_status** | **str** | Reserved for future use.  | [optional] 
**initial_date** | **int** | Reserved for future use. Do not use the &#x60;initialDate&#x60; value for integration development. | [optional] 
**last_modified_device** | [**Device**](Device.md) |  | [optional] 
**marketplace_facilitator_tax_info** | [**MarketplaceFacilitatorTaxInfo**](MarketplaceFacilitatorTaxInfo.md) |  | [optional] 
**pricing_features** | **List[str]** | Pricing features that this order is using. | [optional] 
**server** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**created_date** | **datetime** | The date and time that the Toast platform received the order. | [optional] 

## Example

```python
from toastapi.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


