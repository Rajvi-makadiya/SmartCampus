from flask import render_template

from controllers.student_controllers import student

@student.route('/student-list' , methods=['GET' , 'POST'] , endpoint='student-list')
def student_list():
    return render_template('student/student_list.html')