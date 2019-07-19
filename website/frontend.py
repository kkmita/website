from flask import Blueprint, render_template

from flask import Blueprint, render_template

from website.utils import set_active, caller_name

frontend = Blueprint('frontend', __name__)

website_tabs = [
    {'name': 'Home', 'href': '.home', 'left': True, 'active': ''},
    {'name': 'Projects', 'href': '.projects', 'left': False, 'active': ''},
    {'name': 'Resume', 'href': '.resume', 'left': False, 'active': ''},
    {'name': 'dscussions', 'href': '.dscussions', 'left': False, 'active': ''}
]


@frontend.route('/projects')
def projects():
    tabs = set_active(website_tabs, caller_name())

    return render_template('projects.html', website_tabs=tabs, fname=caller_name())


@frontend.route('/dscussions')
def dscussions():
    tabs = set_active(website_tabs, caller_name())

    return render_template('projects.html', website_tabs=tabs, fname=caller_name())


@frontend.route('/resume')
def resume():
    tabs = set_active(website_tabs, caller_name())

    return render_template('projects.html', website_tabs=tabs, fname=caller_name())


@frontend.route('/')
def home():
    tabs = set_active(website_tabs, caller_name())
    # reset_active_tab(website_tabs)
    # function_name = caller_name()
    # set_active_tab(function_name, website_tabs)

    return render_template('homepage.html', website_tabs=tabs)
