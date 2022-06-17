from sqlalchemy import Column, Integer, String, ForeignKey

from .database import DataBase


class ColorsList(DataBase):
    __tablename__ = "colors_list"
    id = Column(Integer, primary_key=True)
    color_id = Column(Integer, ForeignKey("colors.id"))


class Colors(DataBase):
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
