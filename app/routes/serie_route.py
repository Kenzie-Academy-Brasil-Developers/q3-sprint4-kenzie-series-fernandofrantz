from flask import Blueprint, Flask, request
from app.controllers import serie_controller

bp = Blueprint('series', __name__, url_prefix='/api')

bp.get('/series')(serie_controller.get_series)

# bp.post('/series')(serie_controller.create)


# @bp.get('/series')
# def get_series():
#     return serie_controller.get_series() 

@bp.post('/series')
def post_series():
    new_serie_data = (request.get_json())        
    return serie_controller.create(new_serie_data) 

@bp.get('/series/<int:serie_id>')
def get_specific(serie_id):
    return serie_controller.get_specific_serie(serie_id) 

@bp.get('/table')
def create_table():
    return serie_controller.create_table() 