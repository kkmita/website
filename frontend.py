from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    socialpages = [
        {'link': 'https://www.linkedin.com/', 'icon': 'linkedin'},
        {'link': 'https://www.github.com/kkmita', 'icon': 'github'},
        {'link': 'https://www.stackoverflow.com', 'icon': 'stack-overflow'}
    ]

    return render_template('homepage.html', socialpages=socialpages)
