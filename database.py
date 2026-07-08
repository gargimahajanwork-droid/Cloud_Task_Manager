from sqlalchemy import create_engine
 
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base
import os 

# copy this from neo and replace the username , password and host with your own credentials

# ---FOR DOTENV FILE 
from dotenv import load_dotenv
load_dotenv()
# import the function that can read a .env file , i .e open the new file and load all of its variables , into the memory

DATABASE_URL = os.getenv("DATABASE_URL")




# click show password and copy the complete connection string --before dot env file was loaded

# create SQLALchemy engine 
# the engine is reponsible for connecting fastapi with the cloud Postgresql database 
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

# dependency injection , this function provides a database session whenever an API requires database access 
def get_db():
    db = SessionLocal()

    try: 
        yield db 

    finally:
        db.close()

