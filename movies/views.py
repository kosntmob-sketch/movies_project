from tarfile import data_filter

from django.shortcuts import render, redirect

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
    data_filter = next(item for item in movies_db if movie_slug == item.get('slug'))
    data = {'get_movie':data_filter,
            'movies': movies_db,
            'slug': movie_slug
            }
    return render(request, 'movies/movie.html', context=data)

def genre(request, genre_name):
    #data_filter = [ m for m in movies_db if m.get(genre) == genre_name] по т3 передать отфилтрованный спискок
    return render(request, 'movies/genre.html', context={'movies': movies_db, 'genre_name': genre_name})

def years(request,year):
    print(year)
    return render(request, 'movies/year.html', context={'movies': movies_db})

def old_archive(request):
    return redirect('home', permanent=True)