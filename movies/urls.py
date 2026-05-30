from movies import views
from django.urls import path, register_converter
from movies import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('movie/<slug:movie_slug>/',views.movie, name='movie_detail'),
    path('genre/<str:genre_name>/',views.genre, name='genre_filter'),
    path('years/<year4:year>/', views.years, name='year_filter'),
    path('old-archive/', views.old_archive),
]