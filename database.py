import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dotenv
import os

dotenv.load_dotenv()

driver = os.getenv('DRIVER')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
host_name = os.getenv('HOST_NAME')
db_name = os.getenv('DB_NAME')

DSN = f'{driver}://{login}:{password}@{host_name}/{db_name}'
engine = sa.create_engine(DSN)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
