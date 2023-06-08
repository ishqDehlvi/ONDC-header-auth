import json
import base64
import hashlib
import nacl.encoding
import nacl.signing

# Generate key pairs for signing and encryption
def generate_key_pairs():
    signing_key = nacl.signing.SigningKey.generate()
    signing_public_key = signing_key.verify_key.encode(encoder=nacl.encoding.Base64Encoder).decode()
    signing_private_key = signing_key.encode(encoder=nacl.encoding.Base64Encoder).decode()

    encryption_key = nacl.public.PrivateKey.generate()
    encryption_public_key = encryption_key.public_key.encode(encoder=nacl.encoding.Base64Encoder).decode()
    encryption_private_key = encryption_key.encode(encoder=nacl.encoding.Base64Encoder).decode()

    return {
        'signing_public_key': signing_public_key,
        'signing_private_key': signing_private_key,
        'encryption_public_key': encryption_public_key,
        'encryption_private_key': encryption_private_key,
    }

# Sign a request
def sign_request(json_payload, private_signing_key):
    # Decode the base64-encoded private signing key and add padding if necessary
    padding = len(private_signing_key) % 4
    if padding > 0:
        private_signing_key += '=' * (4 - padding)
    private_signing_key_bytes = base64.urlsafe_b64decode(private_signing_key)

    # Generate UTF-8 byte array from JSON payload
    utf8_payload = json.dumps(json_payload).encode()

    # Generate Blake2b hash from UTF-8 byte array
    digest = hashlib.blake2b(utf8_payload, digest_size=64).digest()

    # Create a signing key from the seed value
    signing_key = nacl.signing.SigningKey(private_signing_key_bytes[:32])

    # Sign the request using the signing key
    signed_message = signing_key.sign(digest, encoder=nacl.encoding.Base64Encoder)

    return signed_message.signature.decode()

# Verify a request
def verify_request(json_payload, authorization_header, signing_public_key):
    # Extract the digest from the encoded signature in the authorization header
    signature = base64.b64decode(authorization_header)

    # Create UTF-8 byte array from the raw payload
    utf8_payload = json.dumps(json_payload).encode()

    # Generate Blake2b hash from UTF-8 byte array
    digest = hashlib.blake2b(utf8_payload, digest_size=64).digest()

    # Verify the generated Blake2b hash with the decoded digest from the signature
    verifying_key = nacl.signing.VerifyKey(signing_public_key, encoder=nacl.encoding.Base64Encoder)
    try:
        verifying_key.verify(digest, signature)
        return True
    except nacl.exceptions.BadSignatureError:
        return False

# Example usage

# Generate key pairs
key_pairs = generate_key_pairs()

# Update the base64 encoded public keys in the registry

# Example JSON payload
json_payload = {
    "country": "IND",
    "city": "*",
    "type": "BPP",
    "subscriber_id": "snoondcogl.snoo.gl",
    "subscriber_url": "https://snoondcogl.snoo.gl",
    "domain": "nic2004:52110",
    "signing_public_key": key_pairs['signing_public_key'],
    "encr_public_key": key_pairs['encryption_public_key'],
    "created": "2023-06-06T21:05:52.470Z2",
    "valid_from": "2023-06-06T21:05:52.470Z3",
    "valid_until": "2050-06-01T11:59:59.470Z7",
    "updated": "2023-06-06T21:05:52.470Z3"
}

# Sign the request
authorization_header = sign_request(json_payload, key_pairs['signing_private_key'])
print("Authorization Header:", authorization_header)

# Verify the request
verification_result = verify_request(json_payload, authorization_header, key_pairs['signing_public_key'])
print("Verification Result:", "Success" if verification_result else "Failure")
