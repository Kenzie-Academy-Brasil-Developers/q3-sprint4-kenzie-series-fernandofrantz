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



        query = 'SELECT * FROM ka_series'

        cur.execute(query)

        series = cur.fetchall()
        print(series)

