from flask import render_template, request, redirect, session, jsonify, json
from flask_bcrypt import Bcrypt
from login_registration_app import app
from login_registration_app.models.User import User

bcrypt = Bcrypt(app)

@app.route("/", methods = ["GET"] )
def registerAndLogin():
    return render_template('index.html')

@app.route("/users/register", methods=["POST"])
def addNewUsers():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"]
    }
    


    #id = request.form[ "first_name", "last_name", "email", "password"  ]
    result = User.save_users( data ) 
    print( result )
    #return result
    return "hello"



#     return redirect ("/")

