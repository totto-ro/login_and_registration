from flask import flash
from login_registration_app.config.MySQLConnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, id, first_name, last_name, email, password, created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password 
        self.created_at = created_at
        self.updated_at = updated_at

    
    @classmethod
    def save_users(cls, data ):
        query = "INSERT INTO users( id, first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL('login_reg_db').query_db(query, data)
        return result

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM users;"
    #     results = connectToMySQL( 'login_reg_db' ).query_db( query )
    #     users = []
    #     for row in results:
    #         users.append( User( row['id'], row['first_name'], row['last_name'], row['email'], row['created_at'], row['updated_at'] ) )
    #     return users

    # @classmethod
    # def get_by_email(cls,data):
    #     query = "SELECT * FROM users WHERE email = %(email)s;"
    #     results = connectToMySQL('login_reg_db').query_db(query,data)
    #     if len(results) < 1:
    #         return False
    #     return cls(results[0])

    # @classmethod
    # def get_by_id(cls,data):
    #     query = "SELECT * FROM users WHERE id = %(id)s;"
    #     results = connectToMySQL('login_reg_db').query_db(query,data)
    #     return cls(results[0])