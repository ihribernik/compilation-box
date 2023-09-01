from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5


def create_access_token(data, expires_delta):
    ...


def verify_password():
    ...
