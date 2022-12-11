from django.urls import path
from typing import List

from . import views

app_name: str = 'posts'

urlpatterns: List = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list')
]
