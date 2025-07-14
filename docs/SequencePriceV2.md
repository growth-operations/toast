# SequencePriceV2

Defines the size, sequence, or size/sequence prices for modifier options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | **int** | Specifies the order of the prices. | [optional] 
**price** | **float** | The price for a modifier option when it is ordered at the specified point in the sequence. | [optional] 

## Example

```python
from toastapi.models.sequence_price_v2 import SequencePriceV2

# TODO update the JSON string below
json = "{}"
# create an instance of SequencePriceV2 from a JSON string
sequence_price_v2_instance = SequencePriceV2.from_json(json)
# print the JSON string representation of the object
print(SequencePriceV2.to_json())

# convert the object into a dict
sequence_price_v2_dict = sequence_price_v2_instance.to_dict()
# create an instance of SequencePriceV2 from a dict
sequence_price_v2_from_dict = SequencePriceV2.from_dict(sequence_price_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


