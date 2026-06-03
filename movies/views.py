from django.shortcuts import render, redirect
from django.http import Http404  # Импортируем для обработки ошибок 404

movies_db = [
    {'id': 1, 'title': 'Интерстеллар', 'slug': 'interstellar', 'year': 2014, 'genre': 'sci-fi',
     'desc': 'Путешествие сквозь черную дыру.'},
    {'id': 2, 'title': 'Начало', 'slug': 'inception', 'year': 2010, 'genre': 'sci-fi',
     'desc': 'Проникновение в чужие сны.'},
    {'id': 3, 'title': 'Зеленая миля', 'slug': 'the-green-mile', 'year': 1999, 'genre': 'drama',
     'desc': 'История в тюрьме Луизианы.'},
    {'id': 4, 'title': 'Побег из Шоушенка', 'slug': 'shawshank', 'year': 1994, 'genre': 'drama',
     'desc': 'История о надежде и дружбе.'},
    {'id': 5, 'title': 'Джентльмены', 'slug': 'the-gentlemen', 'year': 2019, 'genre': 'comedy',
     'desc': 'Криминальный мир Лондона.'},
]


def index(request):
    return render(request, 'movies/index.html', context={'movies': movies_db})


def movie(request, movie_slug):
    # Добавляем None в конец функции next, чтобы избежать падения StopIteration
    data_filter = next((item for item in movies_db if movie_slug == item.get('slug')), None)

    # Если фильм не найден в нашем списке — генерируем честную ошибку 404
    if data_filter is None:
        raise Http404("Фильм не найден")

    data = {
        'get_movie': data_filter,
        'movies': movies_db,
        'slug': movie_slug
    }
    return render(request, 'movies/movie.html', context=data)


def genre(request, genre_name):
    # Реализуем правильную фильтрацию на уровне Python, как вы и хотели!
    data_filter = [m for m in movies_db if m.get('genre') == genre_name]

    # Если такого жанра нет — отправляем на кастомную 404
    if len(data_filter) == 0:
        raise Http404("Жанр не найден")

    return render(request, 'movies/genre.html', context={'movies': data_filter, 'genre_name': genre_name})


def years(request, year):
    data_filter = [m for m in movies_db if m.get('year') == year]

    # Меняем permanent=True на временный редирект (или raise Http404), чтобы не ломать кэш браузера
    if len(data_filter) == 0:
        return redirect('home')

    return render(request, 'movies/year.html', context={'movies': data_filter})


def old_archive(request):
    return redirect('home', permanent=True)


def page_not_found(request, exception):
    return render(request, 'movies/404.html', status=404)