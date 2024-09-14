# from sqlalchemy import select, insert, or_
# from database.models import User
# from core.authenticate.algorithms import hash_password, create_access_token
# from core.database.connection import AsyncSession, db_session
# from core.exceptions.exc import AuthFailedException, BadRequestException, ProccessFailedException, NotFoundException
# from datetime import timedelta
# from core.authenticate.settings import pwd_context
# import jwt
# from jwt import PyJWTError
# from fastapi import Depends
# from fastapi.security import SecurityScopes, HTTPBearer, HTTPAuthorizationCredentials
# from core.redis.commands import check_token_is_in_blacklist



# async def get_user_by_username(db: AsyncSession, username: str):
#     stmt = (
#         select(User)
#         .where(User.username == username)
#     )
#     this_user = (await db.execute(stmt)).scalars().first()
#     if not this_user:
#         raise NotFoundException("User not found")
#     return this_user


# async def register(db: AsyncSession, form_data):
#     request_data = form_data.model_dump(exclude=["password"])
#     stmt = (
#         select(User)
#         .where(
#             or_(
#                 User.email == request_data.get("email"),
#                 User.username == request_data.get("username")
#             )
#         )
#     )
#     old_user = (await db.execute(stmt)).scalars().first()
#     if old_user:
#         raise BadRequestException("User with this data already exist")
#     i_stmt = (
#         insert(User)
#         .values(
#             {
#                 **request_data,
#                 "hashed_password": hash_password(form_data.password)
#             }
#         )
#         .returning(User)
#     )
#     new_user = (await db.execute(i_stmt)).scalars().first()
#     await db.commit()
    
#     if not new_user:
#         raise ProccessFailedException("Register unsuccessfull")
    
#     return new_user



# async def login_user(db: AsyncSession,username: str, password: str):
#     stmt = (
#         select(User)
#         .where(User.username == username)
#     )
#     this_user = (await db.execute(stmt)).scalars().first()
#     if not this_user or not pwd_context.verify(password, this_user.hashed_password):
#         raise AuthFailedException()
    
#     access_token_expires = timedelta(minutes=configs.access_token_expire_minutes)
#     access_token = create_access_token(
#         data={
#             "sub": {
#                 "username": username
#             }
#         },
#         expires_delta=access_token_expires
#     )
    
#     return access_token


# def decode_jwt_token(token: str):
#     try:
#         payload = jwt.decode(token, configs.secret_key, algorithms=[configs.hashing_algorithm])
#         return payload
#     except PyJWTError:
#         raise AuthFailedException("Token is invalid or expired")


# async def check_authentication(
#     security_scopes: SecurityScopes,
#     db: db_session,
#     credentials: HTTPAuthorizationCredentials = Depends(
#         HTTPBearer(auto_error=False)
#     )
# ):
#     if credentials is None:
#         raise AuthFailedException("You are not logged in")
    
#     if await check_token_is_in_blacklist(credentials.credentials):
#         raise AuthFailedException("You are not logged in")

#     decoded_token = decode_jwt_token(credentials.credentials)
#     req_username = decoded_token["sub"]["username"]
#     req_user = await get_user_by_username(db, req_username)
    
#     return {
#         "data": req_user,
#         "token": credentials.credentials,
#         "exp": decoded_token["exp"],
#         "security_scopes": security_scopes.scopes
#     }


