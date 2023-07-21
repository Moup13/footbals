from django.urls import path, re_path

from footobj.views import index, football_list, football_detail, \
    minyfootball_list, minyfootball_detail, searchBar
from django.conf import settings
from django.conf.urls.static import static

app_name = 'footobj'

urlpatterns = [
    path('', index, name = 'index'),
    path('search/', searchBar, name = 'search'),
    path('football/', football_list, name='football'),
    path('football/<id>', football_detail, name='football_detail'),
    path('minyfootball/', minyfootball_list, name='miny_football'),
    path('minyfootball/<id>', minyfootball_detail, name='miny_football'),


    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
