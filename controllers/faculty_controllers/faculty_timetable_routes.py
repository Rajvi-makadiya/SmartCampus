from flask import render_template

from controllers.faculty_controllers import faculty

@faculty.route('/faculty-timetable' , methods=['GET' , 'POST'] , endpoint='faculty-timetable')
def faculty_timetable():
    return render_template('faculty/faculty_timetable.html')