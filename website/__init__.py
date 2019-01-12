import os
from typing import Optional, Dict, Any

from flask import Flask


def create_app(test_config: Optional[Dict[Any, Any]] = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object('instance.Config')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
