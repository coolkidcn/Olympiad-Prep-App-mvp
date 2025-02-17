from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.userMaps, name="userMaps"),
    path('<str:mindMapName>/addDocument/', views.addDocument, name="addDocument"),
    path('create/', views.userMaps, name="create_mindmap")
    path('<str:mindMapName>/', views.userMaps, name="minadMapView"),
]