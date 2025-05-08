from flask import render_template

from controllers.auth_controllers import auth


@auth.route('/forgot-password' , methods=['GET' , 'POST'] , endpoint='forgot-password')
def forgot_password():
    return render_template('auth/forgot.html')

