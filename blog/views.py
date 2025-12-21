from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category


def home(request):
    posts_qs = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts_qs, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(
        request,
        'blog/home.html',
        {
            'posts': posts,
            'categories': categories,
        }
    )


def category_posts(request, id):
    category = get_object_or_404(Category, id=id)
    posts = Post.objects.filter(category=category).order_by('-created_at')

    return render(
        request,
        'blog/category_posts.html',
        {
            'posts': posts,
            'category': category,
        }
    )


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
        }
    )
