# ContentAdvisories

Information about the contents of this menu item or modifier, for example, whether it contains alcohol. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alcohol** | [**Alcohol**](Alcohol.md) |  | [optional] 

## Example

```python
from toastapi.models.content_advisories import ContentAdvisories

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAdvisories from a JSON string
content_advisories_instance = ContentAdvisories.from_json(json)
# print the JSON string representation of the object
print(ContentAdvisories.to_json())

# convert the object into a dict
content_advisories_dict = content_advisories_instance.to_dict()
# create an instance of ContentAdvisories from a dict
content_advisories_from_dict = ContentAdvisories.from_dict(content_advisories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


