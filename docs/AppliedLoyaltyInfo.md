# AppliedLoyaltyInfo

Information about the customer loyalty program account associated with a check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**loyalty_identifier** | **str** | An identifier for the loyalty program account. For &#x60;POST&#x60; orders, this identifier is transmitted to the loyalty program service provider to associate the check with the loyalty account. | [optional] 
**masked_loyalty_identifier** | **str** | A representation of the identifier of the loyalty program account that can be displayed securely. For example: &#x60;************1234&#x60;. The Toast POS displays this string to restaurant employees and guests.  You can optionally include this value when you &#x60;POST&#x60; an order. It is available in response data when you &#x60;GET&#x60; the order.  If you do not provide a &#x60;maskedLoyaltyIdentifier&#x60; when you &#x60;POST&#x60; an order, this value is &#x60;null&#x60; in response data.  The Toast POS app displays a masked representation of the &#x60;loyaltyIdentifier&#x60;. All characters except the last four are hidden.  | [optional] 
**vendor** | **str** | The specific loyalty program service provider that supports the loyalty account. | [optional] 
**accrual_family_guid** | **str** | Response only. An internal Toast platform identifier for loyalty program transactions.  This is not returned from the initial &#x60;POST&#x60; order request and is available at a later time.  | [optional] 
**accrual_text** | **str** | Response only. A description of the loyalty program transaction to print on the customer&#39;s receipt. For example, \&quot;Earned 27 points.\&quot;  The maximum length of the description string is 255 characters.  This is not returned from the initial &#x60;POST&#x60; order request and is available at a later time.  | [optional] 

## Example

```python
from toastapi.models.applied_loyalty_info import AppliedLoyaltyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedLoyaltyInfo from a JSON string
applied_loyalty_info_instance = AppliedLoyaltyInfo.from_json(json)
# print the JSON string representation of the object
print(AppliedLoyaltyInfo.to_json())

# convert the object into a dict
applied_loyalty_info_dict = applied_loyalty_info_instance.to_dict()
# create an instance of AppliedLoyaltyInfo from a dict
applied_loyalty_info_from_dict = AppliedLoyaltyInfo.from_dict(applied_loyalty_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


