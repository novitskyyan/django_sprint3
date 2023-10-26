from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category

from . import constants


def index(request):
    template = 'blog/index.html'
    posts = Post.published_objects.all()[:constants.MAX_NUMBER_POST]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post.published_objects, id=post_id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {'category': category, 'post_list': posts}
    return render(request, template, context)
