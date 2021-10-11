from login_registration_app import app
from flask import render_template,redirect,request,session,flash
from login_registration_app.models.User import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)



@app.route("/")
def form():
    return render_template("index.html")


@app.route('/register', methods=["POST"])
def save_user():

    if not User.validate_register(request.form):
            return redirect('/')
    
    password = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : password
    }
    User.save(data)
    session['email'] = data['email']
    #return "hello"
    return redirect('/dashboard')            

@app.route('/login', methods=["POST"])
def login():
    
    if not User.validate_login(request.form):
            return redirect('/')

    data = {
        "email" : request.form["email"],
        "password" : request.form["password"]
    }

    user= User.email_login(data)
    
    if not user:
        return redirect('/')
    elif not bcrypt.check_password_hash(user.password, data['password']):
        flash("Wrong password! Try again", "login")
        return redirect('/')
    session['email'] = data['email']
    return redirect('/dashboard')  


@app.route("/dashboard")
def read():
    if not 'email' in session:
        flash("You need to login first!", "login")
        return redirect("/")
    
    data={
        'email': session['email']
    }

    result= User.user_by_email(data)
    return render_template("dashboard.html", user=result)

    

@app.route("/logout")
def clearsession():
    session.clear()
    return redirect('/')



