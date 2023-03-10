from flask import Blueprint, request

from .models.factory import Factory
from .models.sprocket import Sprocket
from .response import bad_request, not_found, response

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/factories', methods=['GET'])
def get_factories():
    factories = Factory.query.all()

    return response([factory.serialize() for factory in factories])

@api.route('/factories/<id>', methods=['GET'])
def get_factory(id):
    factory = Factory.query.get(id)

    if factory is None:
        return not_found()
    
    return response(factory.serialize())

@api.route('/sprockets/<id>', methods=['GET'])
def get_sprocket(id):
    sprocket = Sprocket.query.get(id)

    if sprocket is None:
        return not_found()

    return response(sprocket.serialize())

@api.route('/sprockets', methods=['POST'])
def create_sprocket():
    json = request.get_json(force=True)

    if json.get('teeth') is None or json.get('pitch_diameter') is None or json.get('outside_diameter') is None or json.get('pitch') is None:
        return bad_request()
    
    sprocket = Sprocket.new(json.get('teeth'), json.get('pitch_diameter'), json.get('outside_diameter'), json.get('pitch'))

    if sprocket.save():
        return response(sprocket.serialize())
    
    return bad_request()


@api.route('/sprockets/<id>', methods=['PUT'])
def update_sprocket(id):
    sprocket = Sprocket.query.get(id)

    if sprocket is None:
        return not_found()
    
    json = request.get_json(force=True)

    sprocket.teeth = json.get('teeth', sprocket.teeth)
    sprocket.pitch_diameter = json.get('pitch_diameter', sprocket.pitch_diameter)
    sprocket.outside_diameter = json.get('outside_diameter', sprocket.outside_diameter)
    sprocket.pitch = json.get('pitch', sprocket.pitch)

    if sprocket.save():
        return response(sprocket.serialize())
    
    return bad_request()
