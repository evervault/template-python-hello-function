# The Evervault Python SDK (https://docs.evervault.com/reference/python-sdk) is pre-initialized in 
# all Functions as the globally-scoped `evervault` object. This allows you to encrypt the result, 
# and store it in your database.

# `data` is the data you encrypted and passed into `evervault.run` from your server. The Function 
# automatically decrypts the data and maintains its structure so you can treat event exactly as 
# you did when you passed it into `evervault.run`.
def handler(data):
    # Check if the data sent into the Function included the `name` key
    if (data["name"] and isinstance(data["name"], str)):
        print(f'A name of length {len(data["name"])} has arrived into the Function.');


        # Process the decrypted name value, and re-encrypt the original name using the globally available evervault package.
        # Note all Cages have the evervault SDK automatically injected into their global scope.
        return {
            "message": f'Hello from a Function! It seems you have {len(data["name"])} letters in your name',
            "name": f'{evervault.encrypt(data["name"])}',
        }
    else:
        print('An empty name has arrived into the Function.');

        return {
            "message": 'Hello from a Function! Send an encrypted `name` parameter to show Function decryption in action',
        }
