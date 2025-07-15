# ContentAdvisoriesV2

Information about the contents of this menu item or modifier, for example, whether it contains alcohol. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alcohol** | [**AlcoholV2**](AlcoholV2.md) |  | [optional] 

## Example

```python
from toastapi.models.content_advisories_v2 import ContentAdvisoriesV2

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAdvisoriesV2 from a JSON string
content_advisories_v2_instance = ContentAdvisoriesV2.from_json(json)
# print the JSON string representation of the object
print(ContentAdvisoriesV2.to_json())

# convert the object into a dict
content_advisories_v2_dict = content_advisories_v2_instance.to_dict()
# create an instance of ContentAdvisoriesV2 from a dict
content_advisories_v2_from_dict = ContentAdvisoriesV2.from_dict(content_advisories_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


