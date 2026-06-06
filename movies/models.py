from django.db import models

class Director(models.Model):

    name = models.CharField(max_length=50, unique=True)
    # Добавляем слаг для красивых URL
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, verbose_name='URL-слаг')

    class Meta:
        verbose_name = 'Режиссер'

    def __str__(self):
        return self.name



class Actor(models.Model):

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=70, unique=True, verbose_name='Название Фильма')
    year = models.IntegerField(verbose_name='Год выпуска')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL-слаг')
    description = models.TextField(blank=True, verbose_name='Описание фильма')
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return f'{self.title} год выхода: {self.year}'
