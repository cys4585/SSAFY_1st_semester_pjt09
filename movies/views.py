from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Movie, Genre
from django.contrib.auth import get_user_model


user = get_user_model()
# Create your views here.
@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@login_required
@require_GET
def recommended(request):
    print(Movie.objects.filter(genres=request.user.like_genre))
    movies = Movie.objects.filter(genres=request.user.like_genre)[:10]
    # movies = Movie.objects.order_by('-vote_average')[:10]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/recommended.html', context)