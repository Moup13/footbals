from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.template import context
from django.views.generic import ListView, DetailView

from footobj.models import Football, MinyFootball


def index(request):
    return render(request, 'base.html')


def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            football = Football.objects.filter(title__icontains=query)
            miny_football = MinyFootball.objects.filter(title__icontains=query)
            return render(request, 'base.html', {'football':football,
                                                      'miny_football':miny_football,
                                                 })
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})

def football_list(request):
    football = Football.objects.all()
    return render(request, 'footobj/football_list.html', {'football': football})

def football_detail(request, id):
    footballs = Football.objects.get(id=id)

    return render(request, 'footobj/football_detail.html', {'footballs': footballs})



def minyfootball_list(request):
    minyfootball = MinyFootball.objects.all()
    return render(request, 'footobj/minyfootball_list.html', {'minyfootball': minyfootball})

def minyfootball_detail(request, id):
    minyfootballs = MinyFootball.objects.get(id=id)
    return render(request, 'footobj/minyfootball_detail.html', {'minyfootballs': minyfootballs})

















def miny_footballs(request):
    current_link = '/miny_football/'
    one_new = get_object_or_404(Football, link=football)
    response = render(request, 'footobj/minyfootball_list.html', locals())
    response['Cache-Control'] = 'no-cache, must-revalidate'
    return response


