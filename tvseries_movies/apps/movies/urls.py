from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListView.as_view(), name=views.MovieListView.name),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name=views.MovieDetailView.name),
    path('urls/', views.URLListView.as_view(), name=views.URLListView.name),
    path('urls/<int:pk>/', views.URLDetailView.as_view(), name=views.URLDetailView.name),
]