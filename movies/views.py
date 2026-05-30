from django.shortcuts import render
movies_db = [
    {'id': 1, 'title': 'Интерстеллар', 'slug': 'interstellar', 'year': 2014, 'genre': 'sci-fi', 'desc': 'Путешествие сквозь черную дыру.'},
    {'id': 2, 'title': 'Начало', 'slug': 'inception', 'year': 2010, 'genre': 'sci-fi', 'desc': 'Проникновение в чужие сны.'},
    {'id': 3, 'title': 'Зеленая миля', 'slug': 'the-green-mile', 'year': 1999, 'genre': 'drama', 'desc': 'История в тюрьме Луизианы.'},
    {'id': 4, 'title': 'Побег из Шоушенка', 'slug': 'shawshank', 'year': 1994, 'genre': 'drama', 'desc': 'История о надежде и дружбе.'},
    {'id': 5, 'title': 'Джентльмены', 'slug': 'the-gentlemen', 'year': 2019, 'genre': 'comedy', 'desc': 'Криминальный мир Лондона.'},
]
# Create your views here.
def index(request):
    return render(request, 'movies/index.html', context={'movies': movies_db})

def movie(request, movie_slug):
    return render(request, 'movies/movie.html', context={'movies': movies_db, 'slug': movie_slug})

def genre(request, genre_name):
    return render(request, 'movies/genre.html', context={'movies': movies_db, 'genre_name': genre_name})



