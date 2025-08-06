# Payment

Defines a payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**external_id** | **str** | External identifier string that is prefixed by the naming authority. | [optional] 
**paid_date** | **datetime** | The date on which the payment was made. | [optional] 
**paid_business_date** | **int** | The business date (yyyyMMdd) on which this payment was first applied. Response only. | [optional] 
**type** | **str** | The payment method.  When &#x60;POST&#x60;ing, only &#x60;OTHER&#x60; and &#x60;CREDIT&#x60; payment types are supported. For cash payments, you create an external cash payment type in Other Payment Options.  All other types are response only.  Valid values:  * &#x60;CASH&#x60; - The guest paid in cash. * &#x60;CREDIT&#x60; - The guest used a credit card. * &#x60;GIFTCARD&#x60; - The guest used a gift card. * &#x60;HOUSE_ACCOUNT&#x60; - The guest used funds from their house account. * &#x60;REWARDCARD&#x60; - The guest used the available balance on a rewards card. * &#x60;LEVELUP&#x60; - The guest used the LevelUp app. * &#x60;TOAST_SV&#x60; - The guest used their Toast Cash stored value. * &#x60;OTHER&#x60; - The payment type is a custom type configured by the restaurant. * &#x60;UNDETERMINED&#x60; - The payment type cannot be determined.  | 
**card_entry_mode** | **str** | Indicates how credit card data was obtained. Response only.  Valid values:  * &#x60;SWIPED&#x60; - The credit card was swiped through a card reader. * &#x60;KEYED&#x60; - The restaurant employee typed the card number into a device. * &#x60;ONLINE&#x60; - The credit card information was entered online. * &#x60;EMV_CHIP_SIGN&#x60; - The credit card was inserted into a chip reader. * &#x60;TOKENIZED&#x60; - The credit card number is tokenized, meaning that it is replaced by a series of randomly generated numbers. The authorizer is able to use the token to authorize the actual credit card. * &#x60;PRE_AUTHED&#x60; - The credit card was pre-authorized for an initial amount. An example of pre-authorization is swiping a credit card to start a bar tab. The final payment is authorized when the order is complete. * &#x60;SAVED_CARD&#x60; - The credit card information was retrieved from the guest&#39;s account. * &#x60;FUTURE_ORDER&#x60; - The credit card payment was included on a scheduled order. * &#x60;CONTACTLESS&#x60; - The guest used a contactless payment option to provide the credit card number. * &#x60;APPLE_PAY_CNP&#x60; - The guest used the Apple Pay app to make the payment. * &#x60;GOOGLE_PAY_CNP&#x60; - The guest used the Google Pay app to make the payment. * &#x60;INCREMENTAL_PRE_AUTHED&#x60; - An additional payment was added to a pre-authorized card. For example, a guest uses a credit card to open a bar tab. As they continue to order more drinks, the pre-authorized amount is updated. The final payment is authorized when the order is complete. * &#x60;PARTNER_ECOM_COF&#x60; - The restaurant has the credit card on file. * &#x60;CLICK_TO_PAY_CNP&#x60; - The guest used Click to Pay to make the payment.  | [optional] 
**amount** | **float** | The amount of this payment, excluding tips. | 
**tip_amount** | **float** | The amount tipped on this payment. | 
**amount_tendered** | **float** | The amount tendered for this payment. The amount tendered does not include the tip. | [optional] 
**card_type** | **str** | The type of credit card that was used. Response only. | [optional] 
**last4_digits** | **str** | The last 4 digits of the credit card that was used. Response only. | [optional] 
**server** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**refund_status** | **str** | Indicates whether the payment was refunded. Response only.  | [optional] 
**payment_status** | **str** | The status of this payment when the type is &#x60;CREDIT&#x60;. Response only.  | [optional] 
**original_processing_fee** | **float** | The original processing fee for this payment. Populated after the payment is captured. Response only. | [optional] 
**cash_drawer** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**refund** | **object** |  | [optional] 
**void_info** | **object** |  | [optional] 
**house_account** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**other_payment** | [**ExternalReference**](ExternalReference.md) |  | [optional] 
**created_device** | [**Device**](Device.md) |  | [optional] 
**last_modified_device** | **object** |  | [optional] 
**mca_repayment_amount** | **float** | The total currency amount withheld as payments or repayments that apply to your business. For example, the &#x60;mcaRepaymentAmount&#x60; might include:  * Toast Capital payments * Marketplace facilitator tax * Toast Delivery Services costs * Instant deposits  The MCA repayment amount is set at the time the payment is captured, which is typically hours after the actual restaurant guest payment.  Until the &#x60;mcaRepaymentAmount&#x60; is set, this value is &#x60;null&#x60;.  The &#x60;mcaRepaymentAmount&#x60; _might_ be updated when the payment is settled, which is typically one or more days after the actual guest payment. Response only.  You can use the following resources to find more specific information about the payment and repayment amounts that are included in &#x60;mcaRepaymentAmount&#x60;.  * [Toast Capital payments](https://www.toasttab.com/restaurants/admin/capital/) * [Marketplace facilitator tax](https://www.toasttab.com/restaurants/admin/reports/home#sales-summary) * [Marketplace facilitator tax in API data](https://doc.toasttab.com/openapi/orders/tag/Data-definitions/schema/MarketplaceFacilitatorTaxInfo/) * [Instant deposits](https://www.toasttab.com/restaurants/admin/instant-deposit) * [Toast Delivery Services fees and tips](https://www.toasttab.com/restaurants/admin/reports/home#sales-summary) * [Toast Delivery Services fees and tips description](https://www.toasttab.com/restaurants/admin/reports/home#sales-summary)  _Important_: Some of the resources listed here require access to Toast products as a restaurant employee or operator. If your organization provides an integration service you might not have access to the Toast products used by the restaurants you integrate with. Toast support cannot provide access to Toast product information. That information is only available to direct Toast product users.  | [optional] 
**card_payment_id** | **str** | **Note:** this value is in limited release. Your orders API integration might not include the &#x60;cardPaymentId&#x60; value.  A unique identifier for the credit card used for a &#x60;CREDIT&#x60; type payment. The identifier string is generated by the Toast platform and _does not include any information related to or associated with the actual credit card account._ The identifier is unique within your restaurant management group.  The value is &#x60;null&#x60; for the following payment types:  * Payment types other than &#x60;CREDIT&#x60; * Credit card payments entered using EMV (chip cards) * Credit card payments entered by keying in card numbers  Response only.  | [optional] 
**order_guid** | **str** | The Toast platform identifier for the order that contains the payment. Response only. | [optional] 
**check_guid** | **str** | The Toast platform identifier for the check that contains the payment. Response only. | [optional] 
**tender_transaction_guid** | **str** | For internal use only. | [optional] 

## Example

```python
from toastapi.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


