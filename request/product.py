from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    # | None = None make parameter optional.
    buyer_name: str | None = None
    price: int
    vat: int | None = None
    gst: int


class User(BaseModel):
    name: str = Field(title="You can enter your name", description="The name field is required", gt=0)
    email: str
