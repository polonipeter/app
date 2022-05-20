from django.urls import path
from . import views


urlpatterns = [
    path('authorize/', views.authorize_user),
]