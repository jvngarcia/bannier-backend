from pydantic import BaseModel
from pydantic import Field


class Consult( BaseModel ):
    username: str = Field()
    password: str = Field()
