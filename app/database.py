"""
This file handles the connection to the database
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:password@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@' \
                          f'{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)  # responsible for connecting to db

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # models created will extend this base class


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# connect to database using psycopg2
# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost',
#             database='fastAPI',
#             user='postgres',
#             password='mirev',
#             cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()  # to execute SQL statements
#         print("dB connection was successful")
#         break
#     except Exception as error:  # store the exception in variable error
#         print('Connection to dB failed')
#         print(f'Error: {error}')
#         time.sleep(2)  # tries reconnecting to dB every 2 seconds
