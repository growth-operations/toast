# Availability

Information about when a menu is available for use. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_available** | **bool** | Indicates whether this menu is available 24 hours per day, 7 days a week. If &#x60;alwaysAvailable&#x60; is FALSE, then a &#x60;schedule&#x60; value is included in the &#x60;Availability&#x60; object to define the specific times and days a menu is available. If &#x60;alwaysAvailable&#x60; is TRUE, then the &#x60;schedule&#x60; value is omitted.  | [optional] 
**schedule** | [**List[Schedule]**](Schedule.md) | An array of &#x60;Schedule&#x60; objects that indicate the specific days and times a menu is available. If &#x60;alwaysAvailable&#x60; is TRUE, then the menu is available 24 hours per day, 7 days per week, and this &#x60;schedule&#x60; value is omitted from the &#x60;Availability&#x60; object.  | [optional] 

## Example

```python
from toastapi.models.availability import Availability

# TODO update the JSON string below
json = "{}"
# create an instance of Availability from a JSON string
availability_instance = Availability.from_json(json)
# print the JSON string representation of the object
print(Availability.to_json())

# convert the object into a dict
availability_dict = availability_instance.to_dict()
# create an instance of Availability from a dict
availability_from_dict = Availability.from_dict(availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


