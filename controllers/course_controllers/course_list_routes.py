from flask import render_template

from controllers.course_controllers import course

@course.route('/all-course' , methods=['GET'] , endpoint='all-course')
def course_list():
    return render_template('course/course-list.html')

