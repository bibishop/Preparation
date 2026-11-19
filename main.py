from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

from sqlalchemy import create_engine,text
DATABASE_URL = 'postgresql+psycopg2://postgres:Dmail12345@localhost:5432/test'
engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    sql=text("select id,name from person where id>:id")
    rows=conn.execute(sql,{'id':0})
    for row in rows:
        print(row.id,row.name)
class Base(DeclarativeBase):
    pass
class Person(Base):
    __tablename__ = 'person'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    email:Mapped[str|None]=mapped_column(String(255),unique=True)

    def __repr__(self):
        return f"Person(id={self.id},name={self.name!r})"
