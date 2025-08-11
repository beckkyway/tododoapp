from sqlalchemy import ForeignKey, String, BigIntenger
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncAtters, ascync_sessionmaker, create_async_engine

engine = create_async_engine(url ='sqlite+aiosqlite:///db.sqlite3', echo = True)

async_session = ascync_sessionmaker(bind=engine, expire_on_commit=False)


class Base(AsyncAtters,DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigIntenger)

class Task(Base):
     __tablename__ = 'taski'

     id: Mapped[int] = mapped_column(primary_key=True)
     title: Mapped[str] = mapped_column(String(128))
     complited:  Mapped[bool] = mapped_column(default=False)
     user:  Mapped[int] = mapped_column(ForeignKey('users.id', onedelete='CASCADE'))
     
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)