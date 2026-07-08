from sqlalchemy import create_engine
 
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base

# copy this from neo and replace the username , password and host with your own credentials 

DATABASE_URL='postgresql+psycopg2://neondb_owner:npg_DNb4QE0XzxeS@ep-patient-hill-ads375zr-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
# here we are connecting database postgresql databse hosted on the cloud (Neon)
# click show password and copy the complete connection string 

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

