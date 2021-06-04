from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, request, Response
from datetime import datetime

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://test:test@db/test")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    country_code = Column(String(2))
    created_at = Column(DateTime)

    def __init__(self, username: str, country_code: str, created_at: datetime):
        self.username = username
        self.country_code = country_code
        self.created_at = created_at


Base.metadata.create_all(bind=engine)


app = Flask(__name__)


@app.route("/users", methods=["POST"])
def user():
    data = request.json
    db_session.add(
        User(
            username=data["username"],
            country_code=data["country_code"],
            created_at=datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S"),
        )
    )
    db_session.commit()
    return Response(status=200)


app.run(host="0.0.0.0", port=5000)
