from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.userMaps, name="userMaps"),
    #path('<str:mindMapName>/', views.index, name="index"),
]