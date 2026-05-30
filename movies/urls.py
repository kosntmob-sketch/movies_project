from django.urls import path
from movies import views

urlpatterns = [
    path('', views.index, name='home'),
    #path('movie/<slug:movie_slug>/',views.movies, name='movie_detail'),
    #path('genre/<str:genre_name>/',views.genres, name='genre_filter'),
    #path('year/<year4:year>/', views.years, name='year_filter'),
]