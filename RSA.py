#!/usr/bin/env python3
from Crypto.Publickey import RSA

#creation d'un couple de cles
key = RSA.generate(1024)

#chiffrage
public_key = key.publickey()
enc_data = public_key.encrypt(b"""bonjour c'est un message secret""",32)

#afficher ses clés:
k = key.exportKey('PEM')
p = key.publickey().exportKey('PEM')

print(enc_data)
