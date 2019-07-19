from typing import Optional, Dict, Any

from flask import Flask
from flask_bootstrap import Bootstrap

from .frontend import frontend


def create_app(test_config: Optional[Dict[Any, Any]] = None) -> Flask:
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)
    Bootstrap(app)

    app.register_blueprint(frontend)
#    if test_config:
#        app.config.from_mapping(test_config)
#    else:
#        app.config.from_object('instance.Config')

    return app


app = create_app()
