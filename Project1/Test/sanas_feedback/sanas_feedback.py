from sqlalchemy import (
    create_engine,
    Table, Column, Integer, String, Text, DateTime,
    ForeignKey, PrimaryKeyConstraint,
    func, select
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///feedback.sqlite3", echo=True, future=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    message = Column(String, nullable=False)

def main():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()