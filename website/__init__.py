from typing import Optional, Dict, Any

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

def create_app(test_config: Optional[Dict[Any, Any]] = None) -> Flask:
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)
    Bootstrap(app)

#    if test_config:
#        app.config.from_mapping(test_config)
#    else:
#        app.config.from_object('instance.Config')

    return app

app = create_app()

from website import routes

