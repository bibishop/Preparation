from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import create_engine,text
DATABASE_URL = 'postgresql+psycopg2://postgres:Dmail12345@localhost:5432/create_table'
engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    rows = conn.execute(text("""
        SELECT id, first_name, last_name, email, balance
        FROM customers
        ORDER BY id
    """))

from decimal import Decimal
from sqlalchemy import Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    city: Mapped[str | None] = mapped_column(String(50))
    balance: Mapped[Decimal] = mapped_column(Numeric(10, 2))
from sqlalchemy import select
from sqlalchemy.orm import Session
with Session(engine) as session:
    new_customer = Customer(
        first_name="Bekzat",
        last_name="Sadykov",
        email="bekzat@gmail.com",
        city="Bishkek",
        balance=Decimal("15000"),
    )

    session.add(new_customer)
    session.commit()

    print("Customer saved with ID:", new_customer.id)