# Image

Information about an image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | The width of the image, in pixels. | [optional] 
**height** | **int** | The height of the image, in pixels. | [optional] 
**url** | **str** |  | [optional] 
**height_width_ratio** | **float** | The ratio of height to width | [optional] 

## Example

```python
from toastapi.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print(Image.to_json())

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_from_dict = Image.from_dict(image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


