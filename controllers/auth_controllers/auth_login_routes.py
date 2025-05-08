from flask import render_template

from controllers.auth_controllers import auth

@auth.route('/' , methods=['GET' , 'POST'] , endpoint='login')
def login():
    return render_template('auth/signin.html')