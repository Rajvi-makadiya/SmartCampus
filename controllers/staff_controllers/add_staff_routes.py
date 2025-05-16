from flask import render_template

from controllers.staff_controllers import staff

@staff.route('/add-staff' , methods=['GET' , 'POST'] , endpoint='add-staff')
def add_staff():
    return render_template('staff/add_staff.html')