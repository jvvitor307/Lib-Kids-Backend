from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Guardian(Base):
    __tablename__ = "guardians"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(20), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    children = relationship("Child", back_populates="guardian")

class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    guardian_id = Column(Integer, ForeignKey("guardians.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    guardian = relationship("Guardian", back_populates="children")
    rentals = relationship("Rental", back_populates="child")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    photo_base64 = Column(String, nullable=True)
    isbn = Column(String(20), unique=True, nullable=False)

    available_copies = Column(Integer, default=1)
    total_copies = Column(Integer, default=1)

    rentals = relationship("Rental", back_populates="book")

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    child_id = Column(Integer, ForeignKey("children.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    rental_date = Column(DateTime(timezone=True), server_default=func.now())
    expected_rental_date = Column(DateTime(timezone=True), nullable=False)
    return_date = Column(DateTime(timezone=True), nullable=True)

    child = relationship("Child", back_populates="rentals")
    book = relationship("Book", back_populates="rentals")

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
