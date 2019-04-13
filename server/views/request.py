from .api import api
from flask_restplus import Resource


@api.route('/requests')
class Request(Resource):
    def get(self):
        return {'success': False}

    def post(self):
        return {'success': False}


@api.route('/requests/<string:request_id>')
class SingleRequest(Resource):
    def get(self, request_id):
        return {'success': False}


@api.route('/requests/<string:request_id>/comments')
class RequestComments(Resource):
    def get(self, request_id):
        return {'success': False}

    def post(self, request_id):
        return {'success': False}