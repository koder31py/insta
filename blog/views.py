from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post, Profile


def home(request):
    tab = request.GET.get('tab', 'all')

    if request.user.is_authenticated and tab == 'following':
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blog/home.html', {
        'posts': posts,
        'tab': tab
    })


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'blog/register.html', {'error': 'Имя занято'})

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user)
        login(request, user)
        return redirect('home')

    return render(request, 'blog/register.html')


@login_required
def follow_toggle(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)

    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
    else:
        profile.followers.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def create_post(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption', '')

        if image:
            Post.objects.create(
                author=request.user,
                image=image,
                caption=caption
            )
            return redirect('home')

    return render(request, 'blog/create_post.html')
