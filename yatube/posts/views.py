from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post, Group
from typing import TypedDict, List
# Create your views here.


class ContextDict(TypedDict):
    title: str
    posts: List


def index(request: HttpRequest) -> HttpResponse:
    template: str = 'posts/index.html'
    posts: List = Post.objects.order_by('-pub_date')[:10]
    context: ContextDict = {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    template: str = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)

    posts: List = Post.objects.filter(
        group=group).order_by('-pub_date')[:10]
    context: ContextDict = {
        'title': f'Последние записи сообщества {group.title}',
        'posts': posts
    }
    return render(request, template, context)
