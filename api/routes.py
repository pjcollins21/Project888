# flask packages
from flask_restful import Api

# project resources
from api.authentication import SignUpApi, LoginApi
from api.user import UsersApi, UserApi
from api.event import EventsApi, EventApi


def create_routes(api: Api):
    
	# Adds resources to the api.
    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<user_id>')

    api.add_resource(EventsApi, '/event/')
    api.add_resource(EventApi, '/event/<event_id>')