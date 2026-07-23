import logging

from sqlalchemy.orm import Session

from app.auth.security import create_access_token, hash_password, verify_password
from app.db.models import User

logger = logging.getLogger(__name__)


def signup_user(db: Session, email: str, password: str) -> User:
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise ValueError("Email already registered")

    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)

    logger.debug("Created new user: %s", email)

    return user


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.hashed_password):
        return None

    return user


def login_user(db: Session, email: str, password: str) -> str | None:
    user = authenticate_user(db, email, password)
    if not user:
        return None

    return create_access_token(user.id)
