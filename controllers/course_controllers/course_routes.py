from flask import render_template

from controllers.course_controllers import course

@course.route('/add-course' , methods=['GET'] , endpoint='add-course')
def add_course():
    return render_template('course/add_course.html')

