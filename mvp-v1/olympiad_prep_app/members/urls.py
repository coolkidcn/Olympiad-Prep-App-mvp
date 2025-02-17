from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('members/', views.myuser_dashboard, name='myuser_dashboard'),
    path('members/add_Document/', views.add_Document, name='add_Document'),
    path('members/<str:memberName>/', views.user_dashboard, name='user_dashboard'),
    #path("login/", views.login_view, name="login"),
    #path("logout/", views.logout_view, name="logout"),
    #path('dashboard/', views.user_dashboard, name='user_dashboard'),  # Example URL
    #path('document/<int:document_id>/', views.document_detail, name='document_detail'), # Example document detail URL
    #path('document/create/', views.document_create, name='document_create'), # Example document create URL
    #path('mindmap/<int:mindmap_id>/', views.mindmap_detail, name='mindmap_detail'), # Example mindmap detail URL
    #path('mindmap/create/', views.mindmap_create, name='mindmap_create'), # Example mindmap create URL
]
