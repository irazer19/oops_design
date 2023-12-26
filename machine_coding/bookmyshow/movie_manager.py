class MovieManager:
    def __init__(self):
        self.city_movies = {}
        self.movies = []

    def add_movie(self, movie, city):
        if city not in self.city_movies:
            self.city_movies[city] = []
        self.city_movies[city].append(movie)
        self.movies.append(movie)

    def get_movies_by_city(self, city):
        return self.city_movies.get(city, [])

    def get_movies_by_name(self, movie_name):
        for movie in self.movies:
            if movie.movie_name == movie_name:
                return movie
