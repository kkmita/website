import copy
from typing import Dict, Optional

from flask import Blueprint, render_template, url_for

frontend = Blueprint('frontend', __name__)

website_tabs = [
    {'href': '.index', 'active': '', 'name': 'Home'},
    {'href': '.projects', 'active': '', 'name': 'Projects'}
]


def update_active_by_name(name: str, tabs: Optional[Dict[str, str]] = website_tabs):
    output = copy.deepcopy(tabs)

    for tab in output:
        if tab['name'] == name:
            tab['active'] = 'active'

    return output


@frontend.route('/projects')
def projects():
    projects_website_tabs = update_active_by_name('Projects')

    return render_template('projects.html', website_tabs=projects_website_tabs)


@frontend.route('/')
def index():
    home_website_tabs = update_active_by_name('Home')
    # website_tabs = [
    #     {'href': 'https://www.linkedin.com/', 'icon': 'linkedin'},
    #     {'href': 'https://www.github.com/kkmita', 'icon': 'github'},
    #     {'href': 'https://www.stackoverflow.com', 'icon': 'stack-overflow'}
    # ]
    return render_template('homepage.html', website_tabs=home_website_tabs)
