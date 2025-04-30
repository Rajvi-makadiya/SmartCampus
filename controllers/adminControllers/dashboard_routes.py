from flask import render_template

from controllers.adminControllers import admin

@admin.route('/dashboard'  , methods=['GET'] , endpoint='dashboard')
def dashboard():
    return render_template('auth/hy.html')