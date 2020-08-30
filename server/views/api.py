""" Module that contains restx api isntantiation. """
from flask_restx import Api
from config.blueprints import api_v1_blueprint

# Creates a restx api instance
api = Api(api_v1_blueprint)
