from flask import Flask, render_template
from controllers.auth_controllers import auth
from controllers.adminControllers import admin
from controllers.chat_controllers import chat
from controllers.team_controllers import team
from controllers.course_controllers import course
from utiles.config import init_app, db

app = Flask(__name__ , static_folder = 'static')

init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth , url_prefix='/auth')
app.register_blueprint(admin , url_prefix='/admin')
app.register_blueprint(chat , url_prefix='/chat')
app.register_blueprint(team , url_prefix='/team')
app.register_blueprint(course , url_prefix='/course')
@app.route('/')
def login():
    return render_template('auth/signin.html')


if __name__ == '__main__':
    app.run(debug=True)