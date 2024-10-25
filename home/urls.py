from django.urls import path
from . import views

urlpatterns = [

    path('home', views.HomeView.as_view(), name="home.page"),
    path('authorized', views.AuthorizeView.as_view()),
]