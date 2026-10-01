from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from backend.config import CHATBOT_API_KEY


security = HTTPBearer()


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if credentials.credentials != CHATBOT_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )

    return True