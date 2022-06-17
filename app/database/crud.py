from random import shuffle

from sqlalchemy import delete
from sqlalchemy.orm import Session

from . import models, schemas


def delete_colors(db):
    db.execute(delete(models.ColorsList))
    db.commit()


def fill_colors_table(db):
    db_data = db.query(models.Colors).all()
    if not db_data:
        print(db_data)
        color = models.Colors(id=1, name="Синий")
        db.add(color)
        color = models.Colors(id=2, name="Зеленый")
        db.add(color)
        color = models.Colors(id=3, name="Красный")
        db.add(color)
        db.commit()


def set_colors(db):
    fill_colors_table(db)
    temp = []
    for i in range(60):
        temp.append(1)
    for i in range(30):
        temp.append(2)
    for i in range(10):
        temp.append(3)
    shuffle(temp)
    for i in range(len(temp)):
        color_pair = models.ColorsList(id=i, color_id=temp[i])
        db.add(color_pair)
    db.commit()


def get_color_by_id(db, index):
    db_data = db.query(models.ColorsList, models.Colors.name).join(models.Colors).filter(models.ColorsList.id == index).first()
    return db_data.name
