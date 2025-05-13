from flask import render_template

from controllers.library_controllers import library

@library.route('/library-list' , methods=['GET' , 'POST'] , endpoint='library-list')
def assets_list():
    return render_template('library/assets_list.html')

@library.route('/stock-list' , methods=['GET' , 'POST'] , endpoint='stock-list')
def assets_stock_list():
    return render_template('library/assets_stock.html')