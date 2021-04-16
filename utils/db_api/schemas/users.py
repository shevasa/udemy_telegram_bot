from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql


class Users(TimedBaseModel):
    __tablename__="users"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

    referral = Column(BigInteger)

    query: sql.Select

    