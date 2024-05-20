import jwt


def verify_jwt(token_secret_key):
    token = token_secret_key[0]
    secret = token_secret_key[1]
    try:
        decoded = jwt.decode(token, secret, algorithms=['HS384'])
        print(decoded)
    except jwt.exceptions.PyJWTError as e:
        print("Invalid JWT:", e)

