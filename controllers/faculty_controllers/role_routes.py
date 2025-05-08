from flask import render_template

from controllers.faculty_controllers import faculty

@faculty.route('/faculty-role' , methods=['GET'] , endpoint='faculty-course')
def faculty_role():
    return render_template('role.html')