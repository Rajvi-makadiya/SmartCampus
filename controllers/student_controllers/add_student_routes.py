from flask import render_template

from controllers.student_controllers import student

@student.route('/add-student' , methods=['GET' , 'POST'] , endpoint='add-student')
def add_student():
    return render_template('student/add_student.html')