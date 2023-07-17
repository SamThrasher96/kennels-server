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
    return CUSTOMERS

def get_single_customers(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

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