from flask import render_template

from controllers.library_controllers import library

@library.route('/add-library' , methods=['GET' , 'POST'] , endpoint='add-library')
def add_assets():
    return render_template('library/add_assets.html')