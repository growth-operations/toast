# Location

Information about the physical location of a restaurant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | The first line of the street address of the restaurant. | [optional] 
**address2** | **str** | The second line of the street address of the restaurant. | [optional] 
**city** | **str** | The city or town of the restaurant. | [optional] 
**state_code** | **str** | Deprecated. Get the state or province of a restaurant in the &#x60;administrativeArea&#x60; value.  The abbreviation of the state or province of the restaurant.  | [optional] 
**administrative_area** | **str** | The name of the geographical division (for example, state, province, or county) that the restaurant is located in.  | [optional] 
**zip_code** | **str** | The ZIP or postal code of the restaurant. | [optional] 
**country** | **str** | The nation of the restaurant. | [optional] 
**phone** | **str** |  | [optional] 
**phone_country_code** | **str** | A numeric code corresponding to one or more countries, used as a telephone number prefix when making  international telephone calls.  | [optional] 
**latitude** | **float** | The north/south geographic coordinate of the restaurant, in decimal degrees. | [optional] 
**longitude** | **float** | The east/west geographic coordinate of the restaurant, in decimal degrees. | [optional] 

## Example

```python
from toastapi.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


