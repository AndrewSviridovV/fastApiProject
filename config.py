from fastapi import FastAPI
import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

''' FastAPI CONFIGURATION '''
app = FastAPI()


''' DATABASE CONNECTION '''
#DATABASE_URL = "postgresql://rypqppqx:lMK--PkVbssahx106ktkFtP_dY-0blPY@fanny.db.elephantsql.com/rypqppqx"
DATABASE_URL = "postgresql://postgres:Yjdfz_7963@localhost:5432/postgres"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
#Base = declarative_base()
engine = sqlalchemy.create_engine(DATABASE_URL)


''' APP EVENT SETTING'''
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
