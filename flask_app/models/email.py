from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class Email:
    db = "email_schema"
    def __init__(self, data):
        self.id = data['id']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO email (email_address,created_at,updated_at) VALUES (%(email_address)s, NOW(), NOW());"
        return connectToMySQL('email_schema').query_db(query,data)

    @classmethod
    # gets all the authors and returns them in a list of author objects.
    def get_all(cls):
        query = "SELECT * FROM email;"
        results =  connectToMySQL('email_schema').query_db(query)
        emails =[]
        for row in results:
            emails.append(cls(row))
        return emails

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM email WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
        


    @staticmethod
    def validate_email(email):
        is_valid = True 
        query = 'SELECT * FROM email WHERE email_address = %(email_address)s;'
        results = connectToMySQL('email_schema').query_db(query,email)
        if len(results) >= 1:
            is_valid = False
            flash("That email is already in our database.")
        if not EMAIL_REGEX.match(email['email_address']):
            is_valid = False
            flash("Invalid email format")
        if len(email['email_address']) < 1:
            flash("Email address required.")
            is_valid = False
        # if len(dojo['location']) < 1: 
        #     flash("Location is a required field.")
        #     is_valid = False
        # if len(dojo['language']) < 1:
        #     flash("Language is a required field.")
        #     is_valid = False
        # if len(dojo['comment']) < 3 :
        #     flash("Comment is a required field.")
        #     is_valid = False 
        return is_valid 
