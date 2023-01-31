import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import configparser


config = configparser.RawConfigParser() 
config.read('details.properties')
print(config.sections())


try : 
    host = config.get('detailsLocal','host') 
    port = config.get('detailsLocal','port')
    databaseName = config.get('detailsDatabase','dataBaseName')
    Username = config.get('detailsDatabase','Username')
    password = config.get('detailsDatabase','password')
except :
    print("Error while fetching the values from property file -> details.properties")

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(Username,password,host,port,databaseName)
print(DATABASE_URI)

engine = db.create_engine(DATABASE_URI)  # creating engine

Session = sessionmaker(bind=engine)      # making global session 

s = Session()                            # calling off single session from global Session


