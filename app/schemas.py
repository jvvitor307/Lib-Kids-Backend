from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import List, Optional


# ===============================================
#                Book Schemas
# ===============================================

class BaseBook(BaseModel):
    title: str
    author: str
    total_copies: Optional[int]
    available_copies: Optional[int]
    isbn: Optional[str] = None
    photo_base64: Optional[str] = None

class BookCreate(BaseBook):
    pass

class BookUpdate(BaseBook):
    title: Optional[str] = None
    author: Optional[str] = None
    total_copies: Optional[int] = None
    available_copies: Optional[int] = None
    isbn: Optional[str] = None
    photo_base64: Optional[str] = None

class Book(BaseBook):
    id: int

    class Config:
        from_attributes = True


# ===============================================
#                SCHEMAS DE CRIANÇA
# ===============================================

class BaseChild(BaseModel):
    nome: str
    birth_date: date

class ChildCreate(BaseChild):
    pass

class ChildUpdate(BaseModel):
    nome: Optional[str] = None
    birth_date: Optional[date] = None

class Child(BaseChild):
    id: int
    guardian_id: int

    class Config:
        from_attributes = True


