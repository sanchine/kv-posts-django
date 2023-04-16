from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'main_app/index.html', context)


@login_required
def posts(request):
    m_posts = Post.objects.order_by('-like_count')

    context = {
        'title': 'Все посты',
        'posts': m_posts
    }
    return render(request, 'main_app/posts.html', context)


@login_required
def owned_posts(request, owner_id):
    posts = Post.objects.filter(owner=owner_id).order_by('-id')
    user = User.objects.get(id=owner_id)
    context = {
        'title': f'Посты',
        'owner': user.username,
        'owner_id': owner_id,
        'posts': posts
    }
    return render(request, 'main_app/owned_posts.html', context)


@login_required
def post(request, post_id):
    m_post = Post.objects.get(id=post_id)
    context = {
        'title': f'Пост {post_id}',
        'post': m_post
    }
    return render(request, 'main_app/post.html', context)


@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm(files=request.FILES or None)
    else:
        form = PostForm(data=request.POST, files=request.FILES or None)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('main_app:posts')

    context = {
        'title': 'Создание поста',
        'form': form
    }
    return render(request, 'main_app/new_post.html', context)


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        form = PostForm(instance=post, files=request.FILES or None)
    else:
        form = PostForm(instance=post, data=request.POST, files=request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('main_app:post', post_id=post_id)

    context = {
        'title': 'Редактировать пост',
        'post_id': post_id,
        'form': form
    }
    return render(request, 'main_app/edit_post.html', context)


@login_required
def userlist(request):
    users = User.objects.order_by('-id')
    context = {
        'title': 'Список пользователей',
        'users': users
    }
    return render(request, 'main_app/userlist.html', context)

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('main_app:posts')

@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.like_count += 1
    post.save()
    return redirect(f'../../posts/{post.id}')
