from main import engine
from sqlalchemy import text , bindparam 
import datetime as dt
import click

@click.command()
@click.option('--firstName' , prompt = 'Enter the first name : ', help = 'first name')
@click.option('--lastName' , prompt = 'Enter the last name : ',help = 'last name')
@click.option('--address' , prompt = 'Enter the address :',help = 'address')
@click.option('--dob',prompt = 'Enter the DOB', type=click.DateTime(formats=["%Y-%M-%D"]))

with engine.connect() as conn :
    
    # insert 
    '''
    conn.execute(
        text("INSERT INTO customer (first_name,last_name,address,dob,created_by,updated_by) VALUES (:first_name,:last_name,:address,:dob,:created_by,:updated_by)"),
        [{"first_name": 'Dilip', "last_name": 'Mehta', "address": 'Gurgaon', "dob": dt.date(1996, 5, 30), "created_by": dt.datetime.now(), "updated_by": dt.datetime.now()}],
    )
    conn.commit()  
    '''

    # update
    '''
    # update : Change the column data where firstName = Ajay
    # UPDATE user_account SET name=? WHERE user_account.name = ? 
    actualdob = dt.date(1998, 11, 5)
    print(type(actualdob))
    conn.execute(text(f"UPDATE customer SET last_name = 'Kumar' where first_name = 'Ajay'"))
    conn.commit() 
    '''

    # select statement 
    
    records = conn.execute(text("SELECT * FROM customer"))
    for eachRecord in records:
        print(eachRecord) 

    

    # delete statement 
    '''
    st = conn.execute(text("DELETE FROM customer WHERE first_name = 'Dilip'"))
    conn.commit()
    print(st)
    '''

    

