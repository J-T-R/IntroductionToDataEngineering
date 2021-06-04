from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, request, Response

Base = declarative_base()
engine = create_engine("sqlite:///test.db")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)

    def __init__(self, username: str):
        self.username = username


Base.metadata.create_all(bind=engine)


app = Flask(__name__)


@app.route("/users", methods=["POST"])
def user():
    data = request.json
    db_session.add(User(username=data["username"]))
    db_session.commit()
    return Response(status=200)


app.run()
