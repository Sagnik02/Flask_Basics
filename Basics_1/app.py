from flask import Flask, render_template



app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html',name="Sagnik")

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}'

app.run(host='0.0.0.0', port=8080)