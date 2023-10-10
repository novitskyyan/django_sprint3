from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.filter(
        category__is_published=True, is_published=True, pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        id=post_id, pub_date__lte=timezone.now(), is_published=True,
        category__is_published=True
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    posts = category.posts.filter(is_published=True, pub_date__lte=timezone.now())
    context = {'category': category, 'post_list': posts}
    return render(request, template, context)
