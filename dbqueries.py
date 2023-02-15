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

    with engine.connect() as conn:
        operation = conn.execute(sqlStatement , [{"first_name": firstname, "last_name": lastname, "address": address, "dob" : dob, "created_by": dt.datetime.now(), "updated_by": dt.datetime.now()}],)
        logging.debug(operation)
        conn.commit()
    
    logging.info("Data inserted in database")



def select():
    sqlStatement = input('Enter the QUERY')
    with engine.connect() as conn :
        records = conn.execute(text(sqlStatement))
        for eachRecord in records :
            print(eachRecord) 

def update(firstname,lastname,address,dob):
    
    logging.debug(f"firstname :  {firstname} lastname : {lastname} address : {address} dob : {dob}")

    with engine.connect() as conn :

        sqlStatement = text("UPDATE customer SET address = (:address) WHERE first_name = (:first_name)")
        logging.debug(sqlStatement)
        conn.execute(sqlStatement, [{ "address": address, "first_name": firstname}],)
        conn.commit() 

    logging.info("Updated db") 


def delete(firstname,lastname,address,dob):
    sqlStatement = text("DELETE FROM customer WHERE first_name = (:first_name) AND address = (:address)")
    with engine.connect() as conn :
        conn.execute(sqlStatement,[{"first_name" : firstname , "address" : address}],)
        conn.commit() 



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

    

