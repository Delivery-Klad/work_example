from pydantic import BaseModel


class Numbers(BaseModel):
    a: int
    b: int
    c: int
