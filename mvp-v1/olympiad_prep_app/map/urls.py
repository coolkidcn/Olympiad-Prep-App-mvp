from django.urls import include, path
from . import views

urlpatterns = [
    path('create/', views.create_mindmap, name="create_mindmap"),  # Specific path for create
    path('document/<str:document_name>/', views.document_detail, name='document_detail'),
    path('<str:mindMapName>/addDocument/', views.addDocument, name="addDocument"),  # Most specific
    path('<str:mindMapName>/', views.mindmap_detail, name="mindmap_detail"), # Then mindmap detail
    path('', views.userMaps, name="userMaps"),  # Default path last
]
