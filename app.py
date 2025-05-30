from flask import Flask, render_template
from controllers.auth_controllers import auth
from controllers.adminControllers import admin
from controllers.chat_controllers import chat
from controllers.faculty_controllers import faculty
from controllers.staff_controllers import staff
from controllers.student_controllers import student
from controllers.course_controllers import course
from controllers.library_controllers import library
from controllers.hostel_controllers import hostel
from controllers.transport_controllers import transport
from utiles.config import init_app, db

app = Flask(__name__ , static_folder = 'static')

init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth , url_prefix='/auth')
app.register_blueprint(admin , url_prefix='/admin')
app.register_blueprint(chat , url_prefix='/chat')
app.register_blueprint(faculty , url_prefix='/faculty')
app.register_blueprint(staff , url_prefix='/staff')
app.register_blueprint(student , url_prefix='/student')
app.register_blueprint(course , url_prefix='/course')
app.register_blueprint(library , url_prefix='/library')
app.register_blueprint(hostel , url_prefix='/hostel')
app.register_blueprint(transport , url_prefix='/transport')
@app.route('/')
def login():
    return render_template('auth/signin.html')


if __name__ == '__main__':
    app.run(debug=True)