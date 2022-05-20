from django.urls import path
from . import views

urlpatterns = [
    path('authorize/', views.authorize_user),
    path('authorize/get_top', views.get_access),
    path('authorize/get_top/average', views.avegare_count),
    path('authorize/get_top/sort_by_a', views.sort_by_alph),
    path('authorize/get_top/sort_by_i', views.avegare_count),
    path('authorize/get_top/sort_by_p', views.avegare_count),
]