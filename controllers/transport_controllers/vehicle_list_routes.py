from flask import render_template

from controllers.transport_controllers import transport

@transport.route('/vehicle-list' , methods=['GET' , 'POST'] , endpoint='vehicle-list')
def vehicle_list():
    return render_template('transport/vehicle_list.html')

@transport.route('/add-vehicle' , methods=['GET' , 'POST'] , endpoint='add-vehicle')
def add_vehicle():
    return render_template('transport/add_vehicle.html')
