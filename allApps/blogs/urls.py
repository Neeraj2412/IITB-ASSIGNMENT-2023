from django.contrib import admin
from django.urls import path, include
from . import views
from .views import blogsApi

urlpatterns = [
    # path('api_response/', views.apiResponse, name="api_response"),
    # path('api_response/post', views.apiResponsePost, name="api_response_post"),
    path('blog_api/', blogsApi.as_view(), name="blog_api"), # defining the api url
    path('create_post/', views.createBlog, name="create_post"),
    path('list_post/', views.listPost, name="list_post"),
    path('post/<int:id>/', views.particularPost, name="particular_post"),
    path('delete_post/<int:id>/', views.deleteBlog, name="delete_post")
]