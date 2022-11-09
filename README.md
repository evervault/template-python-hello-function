# Hello Function
[Evervault](https://evervault.com) makes it easy to encrypt data at source, process it in a Cage — a secure, serverless function — and never store it unencrypted.

This is a simple Evervault Function example, to help get you up and running on the Evervault platform quickly.

## Getting started with Evervault

Evervault consists of two parts, encrypting your data at source, using either our Node SDK, Python SDK, or Browser and React SDKs and then sending that encrypted data to a Function to be processed securely.

This Function takes a payload that should contain a `name` key. Running the Function is very simple.

## The steps
1. Encrypt your data at source, using one of our SDKs.
2. Process the encrypted data in a Function

### Encrypting at source
```python
# This example uses the Evervault Pyhton SDK.
import evervault

# Initialize the client with your app's API key
evervault.init("<YOUR_API_KEY>")

# Encrypt your data
encrypted = evervault.encrypt({ "name": "Claude" })
```

### Process your encrypted data in a Function
You should encrypt this payload using either our Node SDK, Python SDK, or Browser SDK, then run it in the Hello Function:

```python
# Process the encrypted data in a Function
result = evervault.run("<YOUR_CAGE_NAME>", encrypted)
```

## Understanding the Function
This Function is very simple. Here is the full code:

```python
def handler(data):
    if (data["name"] and isinstance(data["name"], str)):
        print(f'A name of length {len(data["name"])} has arrived into the Function.');

        return {
            "message": f'Hello from a Function! It seems you have {len(data["name"])} letters in your name',
            "name": f'fake call',
        }
    else:
        print('An empty name has arrived into the Function.');

        return {
            "message": 'Hello from a Function! Send an encrypted `name` parameter to show Function decryption in action',
        }
```

Or check it out in [index.js](./index.js).

--- 
If you want to know more about Evervault, check out our [documentation](https://docs.evervault.com).
