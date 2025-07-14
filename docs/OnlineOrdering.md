# OnlineOrdering

Information about the web-based ordering configuration for the restaurant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether the restaurant has enabled the Toast online  ordering module. This value is &#x60;true&#x60; if the module has ever  been enabled. The value _does not_ indicate that a restaurant  is accepting online orders or that the restaurant is using  the Toast online ordering feature.  | [optional] 
**scheduling** | **bool** | Indicates whether the online ordering function for the restaurant allows guests to place orders that will be fulfilled in the future. If this value is &#x60;false&#x60;, orders will be fulfilled as soon as possible.  | [optional] 
**special_requests** | **bool** | Indicates whether the online ordering function for the restaurant allows guests to include written notes with additional instructions for their orders.  | [optional] 
**special_requests_message** | **str** | A written message that is shown to guests when they include additional instructions with an order. For example, the message might be \&quot;no substitutions.\&quot;  | [optional] 
**payment_options** | [**PaymentOptions**](PaymentOptions.md) |  | [optional] 

## Example

```python
from toastapi.models.online_ordering import OnlineOrdering

# TODO update the JSON string below
json = "{}"
# create an instance of OnlineOrdering from a JSON string
online_ordering_instance = OnlineOrdering.from_json(json)
# print the JSON string representation of the object
print(OnlineOrdering.to_json())

# convert the object into a dict
online_ordering_dict = online_ordering_instance.to_dict()
# create an instance of OnlineOrdering from a dict
online_ordering_from_dict = OnlineOrdering.from_dict(online_ordering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


