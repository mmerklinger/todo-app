from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


def create_db() -> SQLAlchemy:
    return SQLAlchemy(model_class=Base)


from todo_app import db


class Tasks(Base):
    __tablename__ = "tasks"
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    description = mapped_column(String)
    open = mapped_column(Boolean, nullable=False)
    user_id = mapped_column(ForeignKey("users.id"))


class Users(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String, nullable=False)
    password = mapped_column(String, nullable=False)
