from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
DATABASE_URL = "postgresql+psycopg2://postgres:Dmail12345@localhost:5432/test"
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str | None] = mapped_column(String(255), unique=True)

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name!r})"


# Create the table if it does not already exist.
Base.metadata.create_all(engine)

with Session(engine) as session:
    user=session.get(Person,1)
    stmt=select(Person).where(Person.name==" Anna")
    anna=session.scalars(stmt).first()
    stmt=(
        select(Person)
        .where(Person.email.is_not(None))
        .order_by(Person.name)
        .limit(10)
    )
    persons=session.scalars(stmt).all()