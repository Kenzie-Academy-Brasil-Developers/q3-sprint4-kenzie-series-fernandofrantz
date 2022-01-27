from flask import jsonify, request
from http import HTTPStatus
from app.models.serie_model import Serie


def get_series():
    Serie.read_series()
    return jsonify({'msg': 'obter series'}), HTTPStatus.OK

def create():
    data = request.get_json()
    return jsonify({'msg': 'criar series'}), HTTPStatus.CREATED