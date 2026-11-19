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
    # Check whether Aida is already in the table.
    person = session.scalar(
        select(Person).where(Person.email == "aida@example.com")
    )

    # Add Aida only if her email is not already present.
    if person is None:
        session.add(Person(name="Aida", email="aida@example.com"))
        session.commit()

    # Read and print all people.
    people = session.scalars(select(Person)).all()

    for person in people:
        print(person.id, person.name, person.email)