import nacl.encoding
import nacl.hash

# Data from the provided JSON
country = "IND"
city = "*"
type_ = "BPP"
subscriber_id = "snoondcogl.snoo.gl"
subscriber_url = "https://snoondcogl.snoo.gl"
domain = "nic2004:52110"
signing_public_key = "ARVbt6qGfrCWdaoqNQfXodgvCOO7XbZf5/Liq0MJwg8="
encr_public_key = "drVJSE7Xh/gBhk4dy/EgNe9M9Qz71BaynaiANIhjkRc="
created = "2023-06-06T21:05:52.470Z2"
valid_from = "2023-06-06T21:05:52.470Z3"
valid_until = "2050-06-01T11:59:59.470Z7"
updated = "2023-06-06T21:05:52.470Z3"

# Step 1: Generate the auth header
auth_header = f'keyId="{subscriber_id}|{domain}|ed25519"'

# Step 2: Generate the payload as a JSON string
payload = {
    "country": country,
    "city": city,
    "type": type_,
    "subscriber_id": subscriber_id,
    "subscriber_url": subscriber_url,
    "domain": domain,
    "signing_public_key": signing_public_key,
    "encr_public_key": encr_public_key,
    "created": created,
    "valid_from": valid_from,
    "valid_until": valid_until,
    "updated": updated
}

# Step 3: Convert the payload to a UTF-8 byte array
payload_bytes = str(payload).encode("utf-8")

# Step 4: Generate the Blake2b hash of the payload
digest = nacl.hash.blake2b(payload_bytes, encoder=nacl.encoding.Base64Encoder)

# Step 5: Add the digest to the authorization header
auth_header += f', digest="{digest.decode()}"'

# Print the auth header
print("Authorization Header:", auth_header)
