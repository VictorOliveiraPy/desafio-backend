from typing import Optional

from fastapi import Header, HTTPException


class AuthenticationMiddleware:
    def __init__(self, api_key_header: str):
        self.api_key_header = api_key_header

    async def __call__(self, api_key: Optional[str] = Header(None)):
        if api_key is None or api_key != self.api_key_header:
            raise HTTPException(status_code=401, detail="Invalid API key")
