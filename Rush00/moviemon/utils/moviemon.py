class Moviemon:
    def __init__(
        self,
        title = "title",
        year = "year",
        director = "director",
        poster = "poster",
        rating = "rating",
        plot = "plot",
        actors = "actors",
    ):
        self.title = title
        self.year = year
        self.director = director
        self.poster = poster
        self.rating = rating
        self.plot = plot
        self.actors = actors

    def __str__(self):
        return str({
            "title": self.title,
            "year": self.year,
            "director": self.director,
            "poster": self.poster,
            "rating": self.rating,
            "plot": self.plot,
            "actors": self.actors,
        })