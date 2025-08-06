# ServiceArea


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**name** | **str** | The name of this service area. | [optional] 
**revenue_center** | [**ExternalReference**](ExternalReference.md) |  | [optional] 

## Example

```python
from toastapi.models.service_area import ServiceArea

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceArea from a JSON string
service_area_instance = ServiceArea.from_json(json)
# print the JSON string representation of the object
print(ServiceArea.to_json())

# convert the object into a dict
service_area_dict = service_area_instance.to_dict()
# create an instance of ServiceArea from a dict
service_area_from_dict = ServiceArea.from_dict(service_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


