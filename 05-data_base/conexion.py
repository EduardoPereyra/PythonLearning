from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_name = 'employees.sqlite'
engine = create_engine(f'sqlite:///{db_name}' )#, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

BaseModel = declarative_base()
