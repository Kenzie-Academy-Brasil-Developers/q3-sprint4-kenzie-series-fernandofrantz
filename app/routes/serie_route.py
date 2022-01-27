from flask import Blueprint, Flask, request
from app.controllers import serie_controller

bp = Blueprint('series', __name__, url_prefix='/api')


bp.get('/series')(serie_controller.get_series)

bp.post('/series')(serie_controller.create)


# @bp.get('/series')
# def get_series():
#     return serie_controller.get_series() 

# @bp.post('/series')
# def post_series():        
#     return serie_controller.create() 


