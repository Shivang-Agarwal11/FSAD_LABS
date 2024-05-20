import jwt
import time
def generate_token():
    global secret
    secret = "Admin@1105"
    payload = {
        "username": "shivang_agarwal11",
        "userID": 102,
        "exp": int(time.time()) + 60 * 60  # Add expiration time (1 hour)
    }
    token = jwt.encode(payload, secret, algorithm='HS384')
    print(token)
    return [token,secret]


