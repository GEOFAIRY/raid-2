from passlib.hash import sha256_crypt

def encrypt(password):
    return sha256_crypt.encrypt(password)

def verify(incoming, saved):
     return sha256_crypt.verify(incoming, saved)