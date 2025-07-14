# MetadataV2

Information about the last date and time that this restaurant's menu data was updated. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restaurant_guid** | **str** | A unique identifier for this restaurant, assigned by the Toast POS system.  | [optional] 
**last_updated** | **str** | The most recent date and time that this menu&#39;s data was published. Use this value to determine if you need to refresh your menu data. The &#x60;lastUpdated&#x60; value uses the absolute timestamp format describe in the &lt;a href&#x3D;\&quot;https://doc.toasttab.com/doc/devguide/api_dates_and_timestamps.html\&quot;&gt;Dates and timestamps&lt;/a&gt; section of the Toast Developer Guide.  | [optional] 

## Example

```python
from toastapi.models.metadata_v2 import MetadataV2

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataV2 from a JSON string
metadata_v2_instance = MetadataV2.from_json(json)
# print the JSON string representation of the object
print(MetadataV2.to_json())

# convert the object into a dict
metadata_v2_dict = metadata_v2_instance.to_dict()
# create an instance of MetadataV2 from a dict
metadata_v2_from_dict = MetadataV2.from_dict(metadata_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


