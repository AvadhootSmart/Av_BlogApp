from django.contrib import admin
from django.urls import path
from BlogPage import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('/ContentBlog/<int:myid>/',views.ContentBlog, name="ContentBlog"),
    path('/User/', views.User, name="User")
]
