from flask import Blueprint

# Create a blueprint for analytics
analytics_blueprint = Blueprint('analytics', __name__)

# Register any routes associated with the analytics blueprint here


def register_blueprints(app):
    app.register_blueprint(analytics_blueprint, url_prefix='/analytics')
