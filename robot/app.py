import falcon

from .images import Resource
from .motor import Motor

api = application = falcon.API()

images = Resource()
motor = Motor()
api.add_route('/images', images)
api.add_route('/motor/{side}',motor)