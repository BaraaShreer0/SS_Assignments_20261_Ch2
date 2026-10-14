from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Original message
message = b"Transfer $1000 to Mark"

# Sign the message with the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Original Message:", message.decode())
print("Digital Signature Generated Successfully")

# Verify the original message
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Original Message: Signature Valid")
except InvalidSignature:
    print("Original Message: Signature Invalid")

# Modify the message and verify again
modified_message = b"Transfer $1000 to Oscar"

try:
    public_key.verify(
        signature,
        modified_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Modified Message: Signature Valid")
except InvalidSignature:
    print("Modified Message: Signature Invalid")