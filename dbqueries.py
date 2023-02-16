from main import engine
from sqlalchemy import text , bindparam 
import datetime as dt
import click
import logging

logging.basicConfig(filename='dbquerieslog.log',level=logging.DEBUG,format='%(levelname)s:%(message)s:%(asctime)s')

def insert(firstname,lastname,address,dob):

    logging.debug(f"firstname :  {firstname} lastname : {lastname} address : {address} dob : {dob}")
    
    sqlStatement = text("INSERT INTO customer (first_name,last_name,address,dob,created_by,updated_by) VALUES (:first_name,:last_name,:address,:dob,:created_by,:updated_by)")
    logging.debug(sqlStatement)
    
    try :
        with engine.connect() as conn:
            operation = conn.execute(sqlStatement , [{"first_name": firstname, "last_name": lastname, "address": address, "dob" : dob, "created_by": dt.datetime.now(), "updated_by": dt.datetime.now()}],)
            logging.info("sql query executed ! Ready for commit")
            conn.commit()  
    except Exception as e :
        logging.exception(f"Operation not performed due to {e}")        
    else :
        logging.info("Data inserted in database")



def select(firstname , lastname , address , dob):

    logging.debug(f"firstname :  {firstname} lastname : {lastname} address : {address} dob : {dob}")
    sqlStatement = text("SELECT * FROM customer WHERE first_name = (:first_name)")

    try :
        with engine.connect() as conn :
            records = conn.execute(sqlStatement,[{"first_name" : firstname }],)
            for eachRecord in records :
                print(eachRecord) 
    except Exception as e :
        logging.exception(f"Operation not performed due to {e}")        
    else :
        logging.info("Data selected from database")

def update(firstname,lastname,address,dob):
    
    logging.debug(f"firstname :  {firstname} lastname : {lastname} address : {address} dob : {dob}")
    sqlStatement = text("UPDATE customer SET address = (:address) WHERE first_name = (:first_name)")

    try :
        with engine.connect() as conn :
            logging.debug(sqlStatement)
            conn.execute(sqlStatement, [{ "address": address, "first_name": firstname}],)
            logging.info("sql query executed ! Ready for commit")
            conn.commit() 
    except Exception as e :
        logging.exception(f"Operation not performed due to {e}")        
    else : 
        logging.info("Data updated in database") 


def delete(firstname,lastname,address,dob):

    logging.debug(f"firstname :  {firstname} lastname : {lastname} address : {address} dob : {dob}")
    sqlStatement = text("DELETE FROM customer WHERE first_name = (:first_name) AND address = (:address)")
    
    try :
        with engine.connect() as conn :
            logging.debug(sqlStatement)
            conn.execute(sqlStatement,[{"first_name" : firstname , "address" : address}],)
            logging.info("sql query executed ! Ready for commit")
            conn.commit()
    except Exception as e :
        logging.exception(f"Operation not performed due to {e}")        
    else : 
        logging.info("Data deletec from database")


if __name__ == '__main__':
    mapping = {"i": insert, "u": update , "s": select, "d": delete}
    
    @click.command()
    @click.option("--toq", default="s")
    @click.option('-fn','--firstname' , help = 'first name')
    @click.option('-ln','--lastname' ,help = 'last name')
    @click.option('-ad','--address' ,help = 'address')
    @click.option('-d','--dob', type=click.DateTime(formats=["%Y-%m-%d"]),default = str(dt.date.today()))
    

    def runner(toq,firstname,lastname,address,dob):
        mapping[toq](firstname,lastname,address,dob)

    runner()         

    

