import json
import base64
import nacl.signing

# Step 1: Generate key pairs
signing_key = nacl.signing.SigningKey.generate()
encryption_key = nacl.signing.SigningKey.generate()

# Step 2: Get the signing and encryption public keys
signing_public_key = signing_key.verify_key
encryption_public_key = encryption_key.verify_key

# Step 3: Convert keys to base64 encoding
signing_public_key_base64 = base64.b64encode(signing_public_key.encode()).decode()
encryption_public_key_base64 = base64.b64encode(encryption_public_key.encode()).decode()

# Step 4: Update the JSON data
registration_data = {
    "country": "IND",
    "city": "*",
    "type": "BPP",
    "subscriber_id": "snoondcogl.snoo.gl",
    "subscriber_url": "https://snoondcogl.snoo.gl",
    "domain": "nic2004:52110",
    "signing_public_key": signing_public_key_base64,
    "encr_public_key": encryption_public_key_base64,
    "created": "2023-06-06T21:05:52.470Z2",
    "valid_from": "2023-06-06T21:05:52.470Z3",
    "valid_until": "2050-06-01T11:59:59.470Z7",
    "updated": "2023-06-06T21:05:52.470Z3"
}

# Print the generated keys and updated JSON data
print("Signing Public Key:", signing_public_key_base64)
print("Encryption Public Key:", encryption_public_key_base64)
print("Updated JSON Data:", registration_data)
