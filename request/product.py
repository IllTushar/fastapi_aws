from pydantic import BaseModel, Field, HttpUrl
from typing import Set, List
from datetime import date, datetime, time, timedelta
from uuid import UUID


class Event(BaseModel):
    id: UUID
    current_date: date
    create_time: datetime
    ending_time: datetime
    repeating_time: time
    execution_time: timedelta


class Item(BaseModel):
    name: str
    # | None = None make parameter optional.
    buyer_name: str | None = None
    price: int
    vat: int | None = None
    gst: int


class Image(BaseModel):
    url: HttpUrl
    name: str


class User(BaseModel):
    name: str = Field(title="You can enter your name", description="The name field is required", gt=0)
    email: str = Field(example="gtushar697@gmail.com")
    tag: Set[str] = []
    image: List[Image]


class Product(BaseModel):
    name: str
    user: User
