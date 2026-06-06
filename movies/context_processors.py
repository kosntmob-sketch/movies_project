from movies.models import Director


def menu_movies(request):
    menu = Director.objects.values_list('name', 'slug')
    return {'menu_list': menu}