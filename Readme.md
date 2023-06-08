## I have implemented this from the ondc official doc(https://docs.google.com/document/d/1fefHfMoYIouN-QJTDJFFZm46dqHmFvwY-6ICoISJcUY/edit#)
Signing & Verification of requests & responses
Key pairs, for signing & encryption, can be generated using libsodium.
Creating key pairs
Create key pairs, for signing (ed25519) & encryption (X25519);
Update base64 encoded public keys in registry;
Utility to generate signing key pairs and test signing & verification is here;
Auth Header Signing
Generate UTF-8 byte array from json payload;
Generate Blake2b hash from UTF-8 byte array;
Create base64 encoding of Blake2b hash, this becomes the digest for signing;
Sign the request, using your private signing key, and add the signature to the request authorization header, following steps documented here;
Auth Header Verification
Extract the digest from the encoded signature in the request;
Get the signing_public_key from registry using lookup (by using the ukId in the authorization header);
Create (UTF-8) byte array from the raw payload and generate Blake2b hash;
Compare generated Blake2b hash with the decoded digest from the signature in the request;
In case of failure to verify, HTTP error 401 should be thrown;