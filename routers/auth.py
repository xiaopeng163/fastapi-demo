
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlmodel import Session, select
from starlette import status

from db import get_session
from schema import UserOutput, User

security = HTTPBasic()


def get_current_user(
    credentials: HTTPBasicCredentials = Depends(security),
    session: Session = Depends(get_session),
) -> UserOutput:

    query = select(User).where(User.username == credentials.username)
    user = session.exec(query).first()
    if user and user.verify_password(credentials.password):
        return UserOutput.from_orm(user)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

