from flask import render_template

from controllers.chat_controllers import chat


@chat.route('/chatapp' , methods=['GET' , 'POST'] , endpoint='chatapp')
def chatapp():
    return render_template('chat/chatapp.html')