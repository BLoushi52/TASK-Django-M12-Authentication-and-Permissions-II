"""theater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies import views as movie_views
from shared import views as shared_views
from users.views import user_register, user_logout, user_login


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", shared_views.home, name="home"),
    path("movies/", movie_views.get_movies, name="movie-list"),
    path("movies/<int:movie_id>/", movie_views.get_movie, name="movie-detail"),
    path("movies/add/", movie_views.create_movie, name="create-movie"),
    path("register_user/",user_register , name="register"),
    path("login/",user_login , name="login"),
    path("logout/",user_logout , name="logout"),
    
    
]
