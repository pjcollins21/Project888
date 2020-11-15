# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.events import Events
from api.errors import forbidden


class EventsApi(Resource):

    # Flask-resftul resource for returning db.event collection.
    @jwt_required
    def get(self) -> Response:

        # GET response method for all documents in events collection.
        output = Events.objects()
        return jsonify({'result': output})

    @jwt_required
    def post(self) -> Response:

        # POST response method for creating event.
        authorized: bool = Events.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Events(**data).save()
            output = {'id': str(post_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()


class EventApi(Resource):

    # Flask-resftul resource for returning db.event collection.
    @jwt_required
    def get(self, event_id: str) -> Response:

        # GET response method for single documents in event collection.
        output = Events.objects.get(id=event_id)
        return jsonify({'result': output})

    @jwt_required
    def put(self, event: str) -> Response:

        # PUT response method for updating an event.
        data = request.get_json()
        put_user = Events.objects(id=event_id).update(**data)
        return jsonify({'result': put_user})

    @jwt_required
    def delete(self, user_id: str) -> Response:

        # DELETE response method for deleting single event.
        authorized: bool = Events.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Events.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()