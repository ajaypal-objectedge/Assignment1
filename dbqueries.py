from main import engine
from sqlalchemy import text 
import datetime as dt
import click
import logging

logging.basicConfig(filename='dbquerieslog.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def insert_assignment1(**params):

    sqlStatement = text("INSERT INTO customer (first_name,last_name,address,dob,created_by,updated_by) VALUES (:first_name,:last_name,:address,:dob,:created_by,:updated_by)")
    query_execution(sqlStatement,**params)       
    logging.info("Data inserted in database")


def select_assignment1(**params):

    sqlStatement = text("SELECT * FROM customer WHERE first_name = (:first_name) AND address = (:address)")
    query_execution(sqlStatement,True,**params)
    logging.info("Data selected from database")

def update_assingment1(**params):
    
    sqlStatement = text(f"UPDATE customer SET address = (:address) , updated_by = (:updated_by)  WHERE first_name = (:first_name)")
    query_execution(sqlStatement,**params)      
    logging.info("Data updated in database") 


def delete_assingment1(**params):

    sqlStatement = text("DELETE FROM customer WHERE first_name = (:first_name) AND address = (:address)")
    query_execution(sqlStatement,**params)
    logging.info("Data deleted from database")

def query_execution(sqlStatement , is_select = False , **params):
    logging.debug(params)
    try :
        with engine.connect() as conn:
            records = conn.execute(sqlStatement , [params],)
            if is_select == True :
                for eachRecord in records :
                    print(eachRecord)
            logging.info("sql query executed ! Ready for commit")
            conn.commit()  
    except Exception as e :
        logging.exception(f"Operation not performed due to {e}")



if __name__ == '__main__':
    mapping = {"i": insert_assignment1, "u": update_assingment1 , "s": select_assignment1, "d": delete_assingment1}
    
    @click.command()
    @click.option("--toq", default="s")
    @click.option('-fn','--firstname' , help = 'first name')
    @click.option('-ln','--lastname' ,help = 'last name')
    @click.option('-ad','--address' ,help = 'address')
    @click.option('-d','--dob', type=click.DateTime(formats=["%Y-%m-%d"]),default = str(dt.date.today()))

    def runner(toq,firstname,lastname,address,dob):
        dict_variables = {
            "first_name": firstname, 
            "last_name": lastname, 
            "address": address, 
            "dob" : dob, 
            "created_by": dt.datetime.now(), 
            "updated_by": dt.datetime.now()
        }
        mapping[toq](**dict_variables)

    runner()         

    

