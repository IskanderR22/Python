

from mysqlconnection import connectToMySQL # This line connects to MYSQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod           # Data is a diotionary containing all the information for the form
    def create(cls, data): # Data allows of to specify WHERE to create, example id
        # Now we run the query in our classmethod, the same as MYSQL
        query = """INSERT INTO users (first_name, last_name, email) 
            VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        user_id =connectToMySQL("users_schema").query_db(query, data) 

        return user_id   
        # This will give us an OBJECT of the mysqlconnection, query the database and
        # Insert the object

    @classmethod # How do we display ALL? Using SELECT * FROM
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query) 
        # Results is ALWAYS a list of dictionaries 

        all_users = []

        for row in results: 
            # Row is each individual dictionary in the results list
            # cls(row) is instantining a Dog Object
            # We are appending it to our list of dog Objects
            all_users.append(cls(row))

        return all_users # The list of Objects 


    @classmethod
    def get_one(cls,data): # Data allows of to specify WHERE to create, example id
        query ="SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_schema").query_db(query, data) 

        # If results is a list of dictionaries
        # Results[0] is the dictionary index of 0

        return cls(results[0])


    @classmethod
    def update(cls, data): # Data allows of to specify WHERE to create, example id
        pass 


    @classmethod
    def delete(cls,data): # Data allows of to specify WHERE to create, example id
        pass
