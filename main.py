import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import configparser
import logging as log

log.basicConfig(filename='dbquerieslog.log',level=log.DEBUG,format='%(levelname)s:%(message)s:%(asctime)s')

try :
    config = configparser.RawConfigParser() 
    config.read('details.properties')
except Exception as e :
    log.exception(f'Unable to read file due to {e}')

try : 
    host = config.get('detailsLocal','host') 
    port = config.get('detailsLocal','port')
    databaseName = config.get('detailsDatabase','dataBaseName')
    Username = config.get('detailsDatabase','Username')
    password = config.get('detailsDatabase','password')
    log.debug(f"host: {host} port: {port} database : {databaseName} Username : {Username} password : {password}")
except Exception as e :
    log.exception("Unable to fetch values from details.properties due to {e}")

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(Username,password,host,port,databaseName)
log.info(DATABASE_URI)

engine = db.create_engine(DATABASE_URI)  # creating engine

Session = sessionmaker(bind=engine)      # making global session 

s = Session()                            # calling off single session from global Session
log.info("Session object called")
print('Main file completed')
