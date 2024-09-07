# from core.authenticate.settings import pwd_context
# from datetime import timedelta, timezone, datetime
# import jwt


# def hash_password(plain_password: str):
#     return pwd_context.hash(plain_password)


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now(timezone.utc) + expires_delta
#     else:
#         expire = datetime.now(timezone.utc) + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, configs.secret_key, algorithm=configs.hashing_algorithm)
#     return encoded_jwt