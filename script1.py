from passlib.hash import sha256_crypt

password = "679780"
hashed_password = sha256_crypt.hash(password)

print(hashed_password)