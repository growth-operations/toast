# Customer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The GUID maintained by the Toast platform. | 
**entity_type** | **str** | The type of object this is. Response only. | 
**first_name** | **str** | The first name, or given name, of the guest.  | 
**last_name** | **str** | The last name, or surname, of the guest.  | 
**phone** | **str** | The telephone number of the guest.  | 
**email** | **str** | The email address corresponding to the guest who placed the order.  | 

## Example

```python
from toastapi.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print(Customer.to_json())

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_from_dict = Customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


