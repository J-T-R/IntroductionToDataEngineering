from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, request, Response
from datetime import datetime
import logging
import json

logging.basicConfig(level=logging.DEBUG)

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
    is_a_dog = Column(Boolean)
    api_version = Column(String(20))

    def __init__(
        self,
        username: str,
        country_code: str,
        created_at: datetime,
        is_a_dog: bool,
        api_version: str = "0.0.1",
    ):
        self.username = username
        self.country_code = country_code
        self.created_at = created_at
        self.is_a_dog = is_a_dog
        self.api_version = api_version


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
            is_a_dog=data.get("is_a_dog", False),
        )
    )

    try:
        db_session.commit()
    except:
        return Response(status=400)

    app.logger.info(
        {
            "username": data["username"],
            "country_code": data["country_code"],
            "created_at": datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S"),
        }
    )
    return Response(status=200)


app.run(host="0.0.0.0", port=5000)
