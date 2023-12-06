from pydantic import BaseModel


class SMessage(BaseModel):
    message: str
