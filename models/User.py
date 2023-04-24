from pydantic import BaseModel


class LoginCreateInput(BaseModel):
    name: str
    password: str

      