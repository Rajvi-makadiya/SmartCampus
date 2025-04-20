from flask import Flask, render_template
app = Flask(__name__ , static_folder = 'static')

@app.route('/')
def login():
    return render_template('auth/signin.html')

@app.route('/forgot')
def forgot_password():
    return render_template('auth/forgot.html')

@app.route('/reset')
def reset_password():
    return render_template('auth/reset-password.html')

@app.route('/chat')
def chat():
    return render_template('chat/chatapp.html')

@app.route('/role')
def role():
    return render_template('role/role.html')

@app.route('/team-list')
def team_list():
    return render_template('staff/team-list.html')

@app.route('/index')
def home():
    return render_template('auth/hy.html')

if __name__ == '__main__':
    app.run(debug=True)