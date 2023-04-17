from typing import Optional

from pydantic import BaseModel


class ErrorResponseSchema(BaseModel):
    error_code: Optional[str] = None
    message: Optional[str] = None