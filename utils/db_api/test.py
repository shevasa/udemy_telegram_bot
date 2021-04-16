import asyncio
import logging

from data import config
from utils.db_api import quick_commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляем пользователя")
    await quick_commands.add_user(1, "Vasya", "vasya@gmail.com")
    await quick_commands.add_user(2, "Petia", "pppetia@gmail.com")
    print("Готово")

    users = await quick_commands.select_all_users()
    print(f"All users: {users=}")

    user = await quick_commands.select_user(id=2)
    print(f"Selected user: {user=}")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(test())
