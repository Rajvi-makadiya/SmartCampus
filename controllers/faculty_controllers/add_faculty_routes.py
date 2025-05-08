from flask import render_template

from controllers.faculty_controllers import faculty

@faculty.route('/add-faculty' , methods=['GET' , 'POST'] , endpoint='add-faculty')
def add_faculty():
    return render_template('faculty/add_faculty.html')