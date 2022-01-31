from http import HTTPStatus

from flask import jsonify
from itsdangerous import json
from app.controllers import serie_controller
from app.models import conn


class Serie:
    def __init__(self, *args, **kwargs) -> None:
        self.serie = kwargs['series']
        self.seasons = kwargs['seasons']
        self.released_date = kwargs['released_date']
        self.genre = kwargs['genre']
        self.imdb_rating = kwargs['imdb_rating']
        
    @staticmethod
    def read_series():
        cur = conn.cursor()

        query_to_create_table = """
        CREATE TABLE IF NOT EXISTS  ka_series(
            id BIGSERIAL PRIMARY KEY,
            serie VARCHAR(100) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULL
        )
        """
        cur.execute(query_to_create_table)
        conn.commit()

        query = 'SELECT * FROM ka_series;'
        cur.execute(query)
        series = cur.fetchall()

        serie_keys = ['id', 'title', 'seasons', 'release_date', 'genre', 'imdb_rating']
        series_list = [dict(zip(serie_keys, ser)) for ser in series]

        cur.close()

        return jsonify(series_list), HTTPStatus.OK


    @staticmethod
    def create(new_serie_data):
        print(new_serie_data)
        
        cur = conn.cursor()

        query_to_create_table = """
        CREATE TABLE IF NOT EXISTS  ka_series(
            id BIGSERIAL PRIMARY KEY,
            serie VARCHAR(100) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULL
        )
        """
        cur.execute(query_to_create_table)
        conn.commit()

        values = (
            new_serie_data['serie'].title(),
            new_serie_data['seasons'],
            new_serie_data['released_date'],
            new_serie_data['genre'].title(),
            new_serie_data['imdb_rating']
            )

        query = f"""
            INSERT INTO 
                ka_series(serie, seasons, released_date, genre, imdb_rating)
            VALUES
                {values}
            RETURNING 
                *;
        """

        cur.execute(query)
        conn.commit()
        serie = cur.fetchall()
        cur.close()
        serie_keys = ['id', 'title', 'seasons', 'release_date', 'genre', 'imdb_rating']
        series_list = [dict(zip(serie_keys, ser)) for ser in serie]

        return jsonify(series_list), HTTPStatus.CREATED


    @staticmethod
    def read_specific_serie(serie_id):
        cur = conn.cursor()

        query_to_create_table = """
        CREATE TABLE IF NOT EXISTS  ka_series(
            id BIGSERIAL PRIMARY KEY,
            serie VARCHAR(100) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULL
        )
        """

        cur.execute(query_to_create_table)
        conn.commit()

        query = 'SELECT * FROM ka_series;'
        cur.execute(query)
        series = cur.fetchall()
        serie_keys = ['id', 'title', 'seasons', 'release_date', 'genre', 'imdb_rating']
        series_list = [dict(zip(serie_keys, ser)) for ser in series]

        cur.close()

        for ser in series_list:
            if (ser['id'] == serie_id):
                return jsonify(ser), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND