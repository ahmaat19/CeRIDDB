from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [

    path('', views.HomeView, name='home'),
    path('projects/', views.ProjectView, name='project'),
    path('projects/add/', views.ProjectCreateView, name='project_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdateView, name='project_update'),
    path('projects/<int:pk>/detail/', views.ProjectDetailView, name='project_detail'),

]