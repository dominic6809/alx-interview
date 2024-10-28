# 0x04-utf8_validation

This project implements a method to validate if a given dataset represents a valid UTF-8 encoding. The dataset is represented as a list of integers, where each integer corresponds to a byte.

## Description

UTF-8 is a variable-length character encoding that can use one to four bytes for each character. This validation function checks if the given data adheres to UTF-8 encoding rules.

## Functionality

The `validUTF8` function verifies the validity of the UTF-8 encoding using the following logic:

- Each character can consist of 1 to 4 bytes.
- Each byte must conform to specific patterns:
  - Single-byte characters start with `0xxxxxxx`.
  - Multi-byte characters must start with `110xxxxx`, `1110xxxx`, or `11110xxx`, followed by bytes that start with `10xxxxxx`.
  
## Prototype

```python
def validUTF8(data):
```

## Parameters
data (List[int]): A list of integers where each integer represents a byte.

## Returns
bool: Returns True if the data is a valid UTF-8 encoding, otherwise returns False.

## Example Usage
To use the validUTF8 function, you can import it and test it with different datasets:
```
from validate_utf8 import validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
```
## Requirements
    Python 3.x
    The code should adhere to PEP 8 style guidelines.
