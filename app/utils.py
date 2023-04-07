from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    """
    this function hashes a password
    """
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    """
    This function verifies if the entered user password matches the
    hashed user password in the db. The password entered by user is
    first hashed and checked against the already stored password in db.
    """
    return pwd_context.verify(plain_password, hashed_password)


