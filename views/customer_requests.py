CUSTOMERS = [
    {
        "id" : 1,
        "name" : "Miguel Morales"
    },
    {
        "id" : 2,
        "name" : "Daniel Cicalese"
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