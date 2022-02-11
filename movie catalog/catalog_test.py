from domain.Movie import Movie
from service.movie_catalog import MovieCatalog

option = None
while option != 4:
    try:
        print('Options: ')
        print('1. Add movie')
        print('2. See listing movies')
        print('3. Delete listing movies file')
        print('4. Exit')
        option = int(input('Type the option please :'))
        if option == 1:
            name_movie = input('Type the name of the movie :')
            movie = Movie(name_movie)
            MovieCatalog.add_movie(movie)
        elif option == 2:
            MovieCatalog.listing_movies()
        elif option == 3:
            MovieCatalog.delete_movies()
    except Exception as e:
        print(f'The error was : {e}')
        print(f'Please, type an option inside of this range 1 - 4 ')

else:
    print('The software has finish with this catalog test')
