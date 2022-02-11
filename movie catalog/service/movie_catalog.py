import os


# os operating system has the method delete

class MovieCatalog:
    variable_path = 'movies.txt'

    # we can use a static method or class method in this case we are going to use a class method because we have a
    # class variable and static method does not have a context class
    @classmethod # static method
    # but we can access directly to our class variable (variable_path )
    def add_movie(cls, movie):
        with open(cls.variable_path, 'a') as file:  # 'a' -> append method
            file.write(f'{movie.name}\n')

    @classmethod
    def listing_movies(cls):
        with open(cls.variable_path, 'r') as file:  # 'r' -> only read
            print('Movie catalog'.center(50, '-'))
            print(file.read())

    @classmethod
    def delete_movies(cls):
        os.remove(cls.variable_path)
        print(f'file deleted: {cls.variable_path}')
