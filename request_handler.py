import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals, get_single_animal, get_single_location, get_all_locations, get_single_employee, get_all_employees, get_single_customers, get_all_customers, create_animal, create_location, create_employee, create_customers, delete_animal, delete_employee, delete_customer, delete_locations, update_animal, update_locations, update_employee, update_customer



# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """


    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            if id is not None:
                animal = get_single_animal(id)
                if animal is not None:
                    self._set_headers(200)
                    response = animal
                else:
                    self._set_headers(404)
                    response = f"Animal {id} is out playing right now"
            else:
                self._set_headers(200)
                response = get_all_animals()

        if resource =="locations":
            if id is not None:
                self._set_headers(200)
                response = get_single_location(id)

            else:
                self._set_headers(200)
                response = get_all_locations()

        if resource =="employees":
            if id is not None:
                self._set_headers(200)
                response = get_single_employee(id)

            else:
                self._set_headers(200)
                response = get_all_employees()

        if resource =="customers":
            if id is not None:
                self._set_headers(200)
                response = get_single_customers(id)

            else:
                self._set_headers(200)
                response = get_all_customers()

        self.wfile.write(json.dumps(response).encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_animal = None
        new_location = None
        new_employee = None
        new_customer = None
        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "animals":
            if "name" in post_body and "species" in post_body and "locationId" in post_body and "customerId" in post_body and "status" in post_body:
                self._set_headers(201)
                new_animal = create_animal(post_body)
        # Encode the new animal and send in response
                response = new_animal
            else:
                self._set_headers(400)
                error_message = ""
                if "name" not in post_body:
                    error_message += "WARNING: name is required."
                if "species" not in post_body:
                    error_message += "WARNING: species is required."
                if "locationId" not in post_body:
                    error_message += "WARNING: location id is required."
                if "customerId" not in post_body:
                    error_message += "WARNING: customer id is required."
                if "status" not in post_body:
                    error_message += "WARNING: status is required."
                new_animal = error_message
                response = new_animal

        if resource == "locations":
            if "name" in post_body and "address" in post_body:
                self._set_headers(201)
                new_location = create_location(post_body)
                response = new_location
            else:
                self._set_headers(400)
                error_message = ""
                if "name" not in post_body:
                    error_message += "WARNING: name is required."
                if "address" not in post_body:
                    error_message += "WARNING: address is required."
                new_location = error_message
                response = new_location

        if resource == "employees":
            if "name" in post_body and "locationId" in post_body and "animalId" in post_body:
                self._set_headers(201)
                new_employee = create_employee(post_body)
                response = new_employee
            else:
                self._set_headers(400)
                error_message = ""
                if "name" not in post_body:
                    error_message += "WARNING: name is required."
                if "locationId" not in post_body:
                    error_message += "WARNING: location id is required."
                if "animalId" not in post_body:
                    error_message += "WARNING: animal id is required."
                new_employee = error_message
                response = new_employee

        if resource == "customers":
            if "name" in post_body and "email" in post_body and "address" in post_body:
                self._set_headers(201)
                new_customer = create_customers(post_body)
                response = new_customer
            else:
                self._set_headers(400)
                error_message = ""
                if "name" not in post_body:
                    error_message += "WARNING: name is required."
                if "email" not in post_body:
                    error_message += "WARNING: email id is required."
                if "address" not in post_body:
                    error_message += "WARNING: address is required."
                new_customer = error_message
                response = new_customer

        
        self.wfile.write(json.dumps(response).encode())


    # A method that handles any PUT request.
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)

        if resource == "locations":
            update_locations(id, post_body)

        if resource == "employees":
            update_employee(id, post_body)

        if resource == "customers":
            update_customer(id, post_body)

    # Encode the new animal and send in response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
    # Set a 204 response code
    # Parse the URL
        (resource, id) = self.parse_url(self.path)

        if resource == "customers":
            self._set_headers(405)
            response = "Warning: Deleting customers is not allowed"
            self.wfile.write(json.dumps(response).encode())
        else:
            self._set_headers(204)
    # Delete a single animal from the list
            if resource == "animals":
                self._set_headers(204)
                delete_animal(id)

            elif resource == "locations":
                self._set_headers(204)
                delete_locations(id)

            elif resource == "employees":
                self._set_headers(204)
                delete_employee(id)

    # Encode the new animal and send in response
        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()

