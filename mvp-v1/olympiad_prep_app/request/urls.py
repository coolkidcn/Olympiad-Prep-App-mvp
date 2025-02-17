from django.urls import path
from . import views

urlpatterns = [
    path('', views.request, name='request'),
    path('map/<str:input>/', views.map, name = 'map'),
    path('<str:input>/', views.aiRequest, name = 'aiRequest'),
    path('recall/<str:input>/', views.recall, name = 'recall'),
]