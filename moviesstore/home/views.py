from django.shortcuts import render
from movies.models import Movie


def index(request):
    template_data = {'title': 'Movies Store'}
    return render(request, 'home/index.html', {'template_data': template_data})


def search(request):
    query = request.GET.get('q', '')
    movies = Movie.objects.filter(name__icontains=query) if query else []

    template_data = {'title': 'Search Results'}
    return render(request, 'home/index.html', {'template_data': template_data, 'movies': movies})

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html',
                  {'template_data': template_data})


