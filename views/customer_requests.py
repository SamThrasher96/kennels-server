import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id" : 1,
        "name" : "Miguel Morales",
        "email": "miguel@gmail.com",
        "address": "123 street",
        "password": "password"
    },
    {
        "id" : 2,
        "name" : "Daniel Cicalese",
        "email": "daniel@gmail.com",
        "address": "123 street",
        "password": "password"
    }
]

def get_all_customers():
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)
        
        customers = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address']
                                , row['email'], row['password'])
            customers.append(customer.__dict__)
            
    return customers

def get_single_customers(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()
        
        customer = Customer(data['id'], data['name'], data['address']
                            , data['email'], data['password'])
        
        return customer.__dict__

def create_customers(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
        
def get_customers_by_email(email):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return customers