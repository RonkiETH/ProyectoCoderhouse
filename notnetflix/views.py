from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Pelicula, Serie, Anime
from .forms import PeliculaForm, SerieForm, AnimeForm

# Create your views here.
def index(request):
    context = {
        'home_active': 'active'
    }
    return render(request, 'home.html', context)

def peliculas(request):
    search_str = request.GET.get('search')
    if search_str:
        peliculas = Pelicula.objects.filter(titulo__icontains=search_str)
    else:
        peliculas = Pelicula.objects.all()

    context = {
        'peliculas_active': 'active',
        'peliculas': peliculas,
    }
    return render(request, 'peliculas.html', context)

def form_peliculas(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        pelicula = Pelicula(
            orden=int(request.POST['orden']),
            titulo=request.POST['titulo'],
            descripcion=request.POST['descripcion'],
        )
        pelicula.save()
        return redirect('peliculas')

    return render(request, 'form_peliculas.html', {'title_h1': 'Pelicula Form'})

def form_peliculas_api(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form_data = PeliculaForm(request.POST)

        if form_data.is_valid:
            data = form_data.cleaned_data

            pelicula = Pelicula(
                orden=data['orden'],
                titulo=data['titulo'],
                descripcion=data['descripcion'],
            )
        pelicula.save()
        return redirect('peliculas')

    return render(request, 'form_peliculas.html', {'title_h1': 'Pelicula Form (API)'})

def series(request):
    search_str = request.GET.get('search')
    if search_str:
        series = Serie.objects.filter(titulo__icontains=search_str)
    else:
        series = Serie.objects.all()

    context = {
        'series_active': 'active',
        'series': series,
    }
    return render(request, 'series.html', context)

def form_series(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        serie = Serie(
            orden=int(request.POST['orden']),
            titulo=request.POST['titulo'],
            descripcion=request.POST['descripcion'],
        )
        serie.save()
        return redirect('series')

    return render(request, 'form_series.html', {'title_h1': 'Series Form'})

def form_series_api(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form_data = SerieForm(request.POST)

        if form_data.is_valid:
            data = form_data.cleaned_data

            serie = Serie(
                orden=data['orden'],
                titulo=data['titulo'],
                descripcion=data['descripcion'],
            )
        serie.save()
        return redirect('peliculas')

    return render(request, 'form_series.html', {'title_h1': 'Series Form (API)'})

def anime(request):
    search_str = request.GET.get('search')
    if search_str:
        anime = Anime.objects.filter(titulo__icontains=search_str)
    else:
        anime = Anime.objects.all()

    context = {
        'anime_active': 'active',
        'anime': anime,
    }
    return render(request, 'anime.html', context)

def form_anime(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        anime = Anime(
            orden=int(request.POST['orden']),
            titulo=request.POST['titulo'],
            descripcion=request.POST['descripcion'],
        )
        anime.save()
        return redirect('anime')

    return render(request, 'form_anime.html', {'title_h1': 'Anime Form'})

def form_anime_api(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form_data = AnimeForm(request.POST)

        if form_data.is_valid:
            data = form_data.cleaned_data

            anime = anime(
                orden=data['orden'],
                titulo=data['titulo'],
                descripcion=data['descripcion'],
            )
        anime.save()
        return redirect('anime')

    return render(request, 'form_anime.html', {'title_h1': 'Anime Form (API)'})
