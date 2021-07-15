
from mysqlconnection import connectToMySQL # This line connects to MYSQL

# This is our MODEL for the database and the purpose is to RETURN an OBJECT!

# The file name should be the same name as the class. 
class Dog:  # We are creating a dog object here
    def __init__(self, data):
        # data is a dictionary that containes all the data from a row in the database.
        # We need an attribute for each field in our table
        self.id = data['id'] # Using the same names as the table field ones
        self.name = ['name']
        self.age = data['age']
        self.hair_color = data['hair_color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    # In general, a CRUD application means 5 methods 
    # Create has 1 method
    # Read has 2 methods 
        # Read Many things, like multiple dogs
        # Read on thing, like one dog
    # Update has 1 method
    # Delete has 1 method
    # All of these methods are classmethods

    @classmethod           # Data is a diotionary containing all the information for the form
    def create(cls, data): # Data allows of to specify WHERE to create, example id
        # Now we run the query in our classmethod, the same as MYSQL
        query = """INSERT  INTO dogs (name, age, hair_color, created_at, updated_at) 
            VALUES (%(name)s, %(age)s, %(hair_color)s, NOW(), NOW());
        """
        dog_id =connectToMySQL("dogs_schema").query_db(query, data) 

        return dog_id   
        # This will give us an OBJECT of the mysqlconnection, query the database and
        # Insert the object

    @classmethod # How do we display ALL? Using SELECT * FROM
    def get_all(cls):
        query = "SELECT * FROM dogs;"
        results = connectToMySQL("dogs_schema").query_db(query) 
        # Results is ALWAYS a list of dictionaries 

        all_dogs = []

        for row in results: 
            # Row is each individual dictionary in the results list
            # cls(row) is instantining a Dog Object
            # We are appending it to our list of dog Objects
            all_dogs.append(cls(row))

        return all_dogs # The list of Objects 


    @classmethod
    def get_one(cls,data): # Data allows of to specify WHERE to create, example id
        query ="SELECT * FROM dogs WHERE id = %(id)s;"
        results = connectToMySQL("dogs_schema").query_db(query, data) 

        # If results is a list of dictionaries
        # Results[0] is the dictionary index of 0

        return cls(results[0])


    @classmethod
    def update(cls, data): # Data allows of to specify WHERE to create, example id
        pass 


    @classmethod
    def delete(cls,data): # Data allows of to specify WHERE to create, example id
        pass


