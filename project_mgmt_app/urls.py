from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myprojects/', views.UserProjects, name='user-projects'),
    path('myprojects/<int:pk>', views.ProjectDetaillView.as_view(), name='project-detail'),
]