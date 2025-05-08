from flask import render_template

from controllers.course_controllers import course

@course.route('/add-subject' , methods=['GET' , 'POST'] , endpoint='add-subject')
def add_subject():
    return render_template('course/add_subject.html')

