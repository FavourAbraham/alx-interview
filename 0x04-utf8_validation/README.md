# 0x04. UTF-8 Validation

## Requirements

### General
- **Editors Allowed**: `vi`, `vim`, `emacs`
- **Environment**: Files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.4.3**
- **File Endings**: Every file should end with a new line
- **Shebang**: The first line of all files should be exactly `#!/usr/bin/python3`
- **PEP 8 Compliance**: Code should follow **PEP 8** style guidelines (version 1.7.x)
- **Executability**: All files must be executable
- **Mandatory README**: A `README.md` file should be present at the root of the project directory

## Tasks

### 0. UTF-8 Validation

**Objective**: Write a method to determine if a data set represents a valid UTF-8 encoding.

- **Prototype**: `def validUTF8(data)`
- **Return Value**: `True` if the data is a valid UTF-8 encoding, otherwise `False`
- **Character Length**: UTF-8 characters can be **1 to 4 bytes** long
- **Multiple Characters**: The data set can contain multiple UTF-8 encoded characters
- **Data Representation**: The input data will be a list of integers, where each integer represents **1 byte** of data. Only the **8 least significant bits** of each integer need to be handled.

#### Example Usage

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Expected output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Expected output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Expected output: False

