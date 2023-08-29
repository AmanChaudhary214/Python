from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post
from .forms import PostForm

# User login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('post_list')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'DjangoApp/login.html')

# User logout view
def user_logout(request):
    logout(request)
    return redirect('post_list')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'DjangoApp/post_list.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the list of posts
    else:
        form = PostForm()
    return render(request, 'DjangoApp/add_post.html', {'form': form})


def edit_post(request, post_id=None):
    if post_id:
        post = get_object_or_404(Post, id=post_id)
    else:
        post = None
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'DjangoApp/edit_post.html', {'form': form})


