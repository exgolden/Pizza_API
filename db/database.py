from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

URL=open("db/postgres.txt", "r")
engine=create_engine(URL.read(), echo=True)
Base=declarative_base()
Session=sessionmaker()
