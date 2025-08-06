# ApplicableDiscountsRequest

A wrapper object that contains an `Order` object and an optional promotional code. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**Order**](Order.md) |  | 
**promo_code** | **str** | An optional promotional code.  | [optional] 

## Example

```python
from toastapi.models.applicable_discounts_request import ApplicableDiscountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicableDiscountsRequest from a JSON string
applicable_discounts_request_instance = ApplicableDiscountsRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicableDiscountsRequest.to_json())

# convert the object into a dict
applicable_discounts_request_dict = applicable_discounts_request_instance.to_dict()
# create an instance of ApplicableDiscountsRequest from a dict
applicable_discounts_request_from_dict = ApplicableDiscountsRequest.from_dict(applicable_discounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


