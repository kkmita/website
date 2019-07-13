from website import app
from flask import render_template

# a simple page that says hello
@app.route('/index')
def hello():
    return render_template('homepage.html')

