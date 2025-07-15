# ImagesV2

Multiple images for a menu item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**high_res_image** | **str** | The URL to a high resolution image. | [optional] 
**image** | **str** | The URL to a standard image. | [optional] 

## Example

```python
from toastapi.models.images_v2 import ImagesV2

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesV2 from a JSON string
images_v2_instance = ImagesV2.from_json(json)
# print the JSON string representation of the object
print(ImagesV2.to_json())

# convert the object into a dict
images_v2_dict = images_v2_instance.to_dict()
# create an instance of ImagesV2 from a dict
images_v2_from_dict = ImagesV2.from_dict(images_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


