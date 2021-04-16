from utils.db_api.db_gino import db
from utils.db_api.schemas.users import Users
from asyncpg import UniqueViolationError


async def add_user(id: int, name: str, email: str):
    try:
        user = Users(id=id, name=name, email=email)
        await user.create()
    except UniqueViolationError:
        pass


async def select_all_users():
    users = await Users.query.gino.all()
    return users


async def select_user(id: int):
    user = await Users.query.where(Users.id == id).gino.first()
    return user


async def count_user():
    total = await db.func.count(Users.id).gino.scalar()
    return total


async def user_email(id, email):
    user = await Users.get(id)
    await user.update(email=email).apply()
    
