# LoyaltyDetails

Information about the loyalty program discount that is applied to a check. The loyalty program account is identified in the `AppliedLoyaltyInfo` value for the check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** | The specific loyalty program service provider that supports the loyalty account. | 
**reference_id** | **str** | The identifier of the loyalty program discount that is recognized by the loyalty program service provider.  The Toast platform transmits the discount identifier to the service provider to determine the validity and amount of the discount.  | 

## Example

```python
from toastapi.models.loyalty_details import LoyaltyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyDetails from a JSON string
loyalty_details_instance = LoyaltyDetails.from_json(json)
# print the JSON string representation of the object
print(LoyaltyDetails.to_json())

# convert the object into a dict
loyalty_details_dict = loyalty_details_instance.to_dict()
# create an instance of LoyaltyDetails from a dict
loyalty_details_from_dict = LoyaltyDetails.from_dict(loyalty_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


