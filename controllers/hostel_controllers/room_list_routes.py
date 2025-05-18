from flask import render_template

from controllers.hostel_controllers import hostel

@hostel.route('/room-list' , methods=['GET' , 'POST'] , endpoint='room-list')
def room_list():
    return render_template('hostel/room_list.html')

@hostel.route('/add-room' , methods=['GET' , 'POST'] , endpoint='add-room')
def add_room():
    return render_template('hostel/add_room.html')