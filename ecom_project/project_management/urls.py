from django.urls import path
from . import views

urlpatterns = [
	path('project-management', views.ProjectManagement),
]
