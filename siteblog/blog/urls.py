from django.urls import path

from blog.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
]
