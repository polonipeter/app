from django.urls import path
from . import views


urlpatterns = [
    path('authorize/', views.authorize_user),
    path('authorize/get_top', views.get_access),
    path('authorize/get_top/average', views.avegare_count),
]