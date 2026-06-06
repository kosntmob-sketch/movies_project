from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404  # Импортируем для обработки ошибок 404
from .models import Movie, Director, Actor



def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', context={'movies': movies})


def movie(request, movie_slug):
    movies = Movie.objects.all()
    data_filter = get_object_or_404(Movie, slug=movie_slug)

    data = {
        'get_movie': data_filter,
        'movies': movies,
        'slug': movie_slug
    }
    return render(request, 'movies/movie.html', context=data)


def director_movies(request, director_id):

    director = get_object_or_404(Director, slug=director_id)
    print(director_id)
    data_filter = director.movies.all()




    return render(request, 'movies/genre.html', context={'movies': data_filter, 'director': director})


def years(request, year):
    data_filter = Movie.objects.filter(year=year)
    if not data_filter.exists():
        raise Http404("Фильмы за этот год не найдены")
    return render(request, 'movies/year.html', context={'movies': data_filter})


def old_archive(request):
    return redirect('home', permanent=True)


def page_not_found(request, exception):
    return render(request, 'movies/404.html', status=404)