from flask import render_template

from controllers.faculty_controllers import faculty

@faculty.route('/faculty-list' , methods=['GET' , 'POST'] , endpoint='faculty-list')
def faculty_list():
    return render_template('faculty/faculty-list.html')