from flask import Flask, render_template

app = Flask(__name__ , static_folder = 'static')

@app.route('/')
def login():
    return render_template('auth/signin-2.html')

@app.route('/forgot')
def forgot_password():
    return render_template('auth/forgot-2.html')

if __name__ == '__main__':
    app.run(debug=True)