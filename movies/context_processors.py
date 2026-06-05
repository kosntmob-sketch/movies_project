from movies.models import Director


def menu_movies(request):
    menu = Director.objects.values_list('name', flat=True)
    return {'menu_list': menu}