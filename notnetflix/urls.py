from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('listar/peliculas', views.peliculas, name='peliculas'),
    path('form/peliculas', views.form_peliculas, name='form_peliculas'),
    path('form-api/peliculas', views.form_peliculas_api, name='form_peliculas_api'),
    path('listar/series', views.series, name='series'),
    path('form/series', views.form_series, name='form_series'),
    path('form-api/series', views.form_series_api, name='form_series_api'),
    path('listar/anime', views.anime, name='anime'),
    path('form/anime', views.form_anime, name='form_anime'),
    path('form-api/anime', views.form_anime_api, name='form_anime_api'),
]
