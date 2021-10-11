from flask import Flask
from login_registration_app import app
from login_registration_app.controllers import users_controller

if __name__ == "__main__":
    app.run( debug = True )