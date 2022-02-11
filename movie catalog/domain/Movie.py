class Movie:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f'Name of the movie :{self._name}'

    # get method
    @property
    def name(self):
        return self._name

    # set method
    @name.setter
    def name(self, name):
        self._name = name


#movie = Movie(name='harry potter')
#print(movie)