# SequencePrice

Defines pricing based on sequence for modifier options in a modifier group. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | **int** | The sequence number for this pricing rule.  | [optional] 
**price** | **float** | The price for modifier options at this sequence position.  | [optional] 

## Example

```python
from toastapi.models.sequence_price import SequencePrice

# TODO update the JSON string below
json = "{}"
# create an instance of SequencePrice from a JSON string
sequence_price_instance = SequencePrice.from_json(json)
# print the JSON string representation of the object
print(SequencePrice.to_json())

# convert the object into a dict
sequence_price_dict = sequence_price_instance.to_dict()
# create an instance of SequencePrice from a dict
sequence_price_from_dict = SequencePrice.from_dict(sequence_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


