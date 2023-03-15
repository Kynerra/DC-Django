from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('anime-detail/<int:id>/', anime_detail_view, name='anime_detail_url'),
    path('search/<int:page>/', search_view, name='search_url'),
    path('trending-now/<int:page>/', trending_all_view, name='trending_all_url'),
    path('trending-now/', trending_all_nopage_view),
    path('recently-added/<int:page>/', recent_all_view, name='recent_all_url'),
    path('recently-added/', recent_all_nopage_view),
    path('anime-wathcing/<int:id>/ep-<int:ep>/', anime_watching_view, name='anime_watching_url')
]