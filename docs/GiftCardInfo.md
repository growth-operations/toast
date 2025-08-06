# GiftCardInfo

Reserved for future use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**last4_card_digits** | **str** | The last 4 digits of the gift card that was used. | 
**first5_card_digits** | **str** | The first 5 digits of the gift card that was used. Response only. | [optional] 

## Example

```python
from toastapi.models.gift_card_info import GiftCardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardInfo from a JSON string
gift_card_info_instance = GiftCardInfo.from_json(json)
# print the JSON string representation of the object
print(GiftCardInfo.to_json())

# convert the object into a dict
gift_card_info_dict = gift_card_info_instance.to_dict()
# create an instance of GiftCardInfo from a dict
gift_card_info_from_dict = GiftCardInfo.from_dict(gift_card_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


