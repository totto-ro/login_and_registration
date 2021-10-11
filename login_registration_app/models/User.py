from flask import flash
from login_registration_app.config.MySQLConnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s ,%(password)s, NOW() , NOW() );"
        return connectToMySQL('login_reg_db').query_db( query, data )
    
    @classmethod
    def email_login(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        user = connectToMySQL('login_reg_db').query_db(query,data)
        if len(user) < 1:
            flash("Email not found. Please register", "login")
            return False
        print(user)
        return cls(user[0])

    @classmethod
    def user_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('login_reg_db').query_db(query,data)
        print (result)
        return User(result[0])


    @staticmethod
    def validate_user( user ):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        if len(user['first_name']) < 1:
            flash("First Name must be at least 1 character.", "register")
            is_valid = False
        if len(user['last_name']) < 1:
            flash("Last Name must be at least 1 character.", "register")
            is_valid = False
        if len(user['password']) < 3:
            flash("Password must be at least 3 characters.", "register")
            is_valid = False
        if len( connectToMySQL( 'login_reg_db' ).query_db( query,user ))>0:
            flash("This email is already registered in our database.", "register")
            is_valid=False
        if user['password'] != user['confirm']:
            flash("Your confirm password doesn't match the password", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login( user ):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "login")
            is_valid = False
        if len(user['password']) < 5:
            flash("Password must be at least 5 characters.", "login")
            is_valid = False
        return is_valid