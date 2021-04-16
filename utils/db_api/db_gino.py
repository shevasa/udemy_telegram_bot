import logging

from gino import Gino
import sqlalchemy as sa
from sqlalchemy import Column, DateTime
from aiogram import Dispatcher

from data import config

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        from typing import List
        primary_key_columns: List[sa.Column] = table.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=db.func.now())
    updated_at = Column(DateTime(True),
                        default=db.func.now(),
                        server_default=db.func.now(),
                        onupdate=db.func.now())


async def on_startup(dispatcher: Dispatcher):
    logging.info("Подключение к PostgreSQL")
    await db.set_bind(config.POSTGRES_URI)