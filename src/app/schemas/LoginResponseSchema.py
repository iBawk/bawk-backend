import re
from pydantic import BaseModel, validator


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
