from flask import render_template

from controllers.hostel_controllers import hostel

@hostel.route('/room-type' , methods=['GET' , 'POST'] , endpoint='room-type')
def room_type():
    return render_template('hostel/room_type.html')

@hostel.route('/add-type' , methods=['GET' , 'POST'] , endpoint='add-type')
def add_type():
    return render_template('hostel/add_type.html')