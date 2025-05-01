from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    detail: str = Field(name="Detail", description="The result of the query.")
