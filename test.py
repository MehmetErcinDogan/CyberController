import hashlib

id = str("admin")
id = id.encode()
id = hashlib.sha256(id)
id = id.hexdigest()

print(id)