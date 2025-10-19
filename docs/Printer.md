# Printer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | [optional] 
**entity_type** | **str** | The type of object this is. Response only. | [optional] 
**name** | **str** | The name of the printer. | [optional] 

## Example

```python
from toastapi.models.printer import Printer

# TODO update the JSON string below
json = "{}"
# create an instance of Printer from a JSON string
printer_instance = Printer.from_json(json)
# print the JSON string representation of the object
print(Printer.to_json())

# convert the object into a dict
printer_dict = printer_instance.to_dict()
# create an instance of Printer from a dict
printer_from_dict = Printer.from_dict(printer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


