from generate_jwt import generate_token
from verify_jwt import verify_jwt

token_secret_key = generate_token()
verify_jwt(token_secret_key)