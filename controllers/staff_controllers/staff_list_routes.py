from flask import render_template

from controllers.staff_controllers import staff

@staff.route('/staff-list' , methods=['GET' , 'POST'] , endpoint='staff-list')
def staff_list():
    return render_template('staff/staff_list.html')