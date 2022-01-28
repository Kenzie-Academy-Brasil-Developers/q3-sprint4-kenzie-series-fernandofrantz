from flask import jsonify, request
from http import HTTPStatus
from app.models.serie_model import Serie


def get_series():
    return Serie.read_series()

def create(new_serie_data):
    return Serie.create(new_serie_data)

def get_specific_serie(serie_id):
    return Serie.read_specific_serie(serie_id)

def create_table():
    return Serie.create_table()