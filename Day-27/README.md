# Day-27 Password Manager

This is a simple password manager implemented in Python using the `cryptography` library. It allows you to securely store and retrieve passwords for different sites.

## Features

- Generate a secure encryption key.
- Encrypt and store passwords.
- Retrieve and decrypt stored passwords.
- Generate random secure passwords.

## Requirements

- Python 3.6 or higher
- `cryptography` library

## Installation

To install the required `cryptography` library, use the following command:

```sh
pip install cryptography
```

## Usage

### 1. Generate and Save an Encryption Key

First, generate a new encryption key and save it to a file named `key.key`.

```python
key = generate_key()
save_key(key)
```

### 2. Store a Password

To store a password for a specific site, use the `store_password` function. This function encrypts the password and saves it in the `passwords.txt` file.

```python
store_password('Facebook', generate_password())
store_password('Instagram', generate_password())
```

### 3. Retrieve a Password

To retrieve a password for a specific site, use the `retrieve_password` function. This function decrypts the password and returns it.

```python
retrieved_password = retrieve_password('Facebook')
print(retrieved_password)
```

### Complete Example

Here is a complete example of how to use the password manager:

```python
from cryptography.fernet import Fernet
import os
import string
import secrets

def generate_key():
    # Generate a key and return it as bytes
    return Fernet.generate_key()

def load_key():
    # Load the key from a file
    with open('key.key', 'rb') as file:
        key = file.read()
    return key

def save_key(key):
    # Save the key to a file in binary mode
    with open('key.key', 'wb') as file:
        file.write(key)

def encrypt_password(password, key):
    # Create a Fernet cipher suite with the given key
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password.decode()

def decrypt_password(encrypted_password, key):
    # Create a Fernet cipher suite with the given key
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
    return decrypted_password.decode()

def store_password(site, password):
    key = load_key()
    encrypted_password = encrypt_password(password, key)
    with open('passwords.txt', 'a') as file:
        file.write(f'{site}:{encrypted_password}\n')

def retrieve_password(site):
    key = load_key()
    with open('passwords.txt', 'r') as file:
        for line in file:
            data = line.strip().split(':')
            if data[0] == site:
                encrypted_password = data[1]
                return decrypt_password(encrypted_password, key)
    return None

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Usage example
key = generate_key()
save_key(key)

store_password('Facebook', generate_password())
store_password('Instagram', generate_password())

retrieved_password = retrieve_password('Facebook')
print(retrieved_password)
```

## Explanation of File Storage

### `key.key`
This file stores the encryption key used to encrypt and decrypt the passwords. It is crucial to keep this file secure and not share it with anyone. If this key is lost, you will not be able to decrypt your stored passwords.

### `passwords.txt`
This file stores the encrypted passwords. Each line in this file represents a site and its corresponding encrypted password in the following format:

```
site:encrypted_password
```

For example:

```
Facebook:gAAAAABgVZg....
Instagram:gAAAAABgXkC....
```

Make sure to keep this file secure as well since it contains your sensitive data.

## Security Note

Always ensure that both the `key.key` and `passwords.txt` files are stored in a secure location. If these files are accessed by an unauthorized person, they could potentially decrypt your stored passwords. It's also recommended to use a strong master password for encrypting the key if implementing further security measures.

---
