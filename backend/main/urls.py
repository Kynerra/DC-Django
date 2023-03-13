from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('anime-detail/<int:id>/', anime_detail_view, name='anime_detail_url'),
    path('search/<int:page>/', search_view, name='search_url'),
]