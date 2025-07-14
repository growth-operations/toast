# URLs

Web addresses for the restaurant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website** | **str** | The primary website for the restaurant. | [optional] 
**facebook** | **str** | A Facebook™ page for the restaurant. | [optional] 
**twitter** | **str** | A Twitter™ handle for the restaurant. | [optional] 
**order_online** | **str** | A URL for the online ordering site for the restaurant. | [optional] 
**purchase_gift_card** | **str** | A URL for the gift card purchasing site for the restaurant. | [optional] 
**check_gift_card** | **str** | A URL for a site at which guests can find balances and other information about gift cards. | [optional] 

## Example

```python
from toastapi.models.urls import URLs

# TODO update the JSON string below
json = "{}"
# create an instance of URLs from a JSON string
urls_instance = URLs.from_json(json)
# print the JSON string representation of the object
print(URLs.to_json())

# convert the object into a dict
urls_dict = urls_instance.to_dict()
# create an instance of URLs from a dict
urls_from_dict = URLs.from_dict(urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


