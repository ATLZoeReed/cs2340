from django.shortcuts import render
from movies.models import Movie
import datetime

def index(request):
    search_term = request.GET.get('search', '')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
        type = "search"
    else:
        movies = Movie.objects.order_by('date')
        if len(movies) > 5:
            movies = movies[len(movies) - 5:]
        movies.reverse()
        type = "recent"
    print(search_term, movies)
    template_data = {'title': 'Movies Store', 'movies': movies, 'search_term': search_term, 'type': type}
    return render(request, 'home/index.html', {'template_data': template_data})

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html',
                  {'template_data': template_data})


