from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .models import Image
from core.models import Image
from django.utils import timezone


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'core/register.html', {'error': 'Username already exists'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')  # Make sure 'login' URL name exists
    return render(request, 'core/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

@login_required
def dashboard(request):
    user_posts = Post.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'core/dashboard.html', {'form': form, 'posts': user_posts})

def logout_view(request):
    logout(request)
    return redirect('login')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assign the current logged-in user
            post.save()
            return redirect('user_posts')  # Redirect to a page where posts are displayed
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})

def user_posts(request):
    posts = Post.objects.all()
    return render(request, 'user_posts.html', {'posts': posts})

@login_required
def like_image(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('home')

@login_required
def profile(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'core/profile.html', {'images': images})
