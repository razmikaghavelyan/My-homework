from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Post, Topic, Message, User
from .forms import PostForm, UserForm, MyUserCreationForm
from django.shortcuts import get_object_or_404


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    posts = user.post_set.all()
    post_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'posts': posts,
               'post_messages': post_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    posts = Post.objects.filter(
        Q(topic__name__icontains=q) |
        Q(description__icontains=q) |
        Q(photo__icontains=q)

    )

    topics = Topic.objects.all()[0:5]
    post_count = posts.count()
    post_messages = Message.objects.filter(
        Q(post__topic__name__icontains=q))[0:3]
    context = {'posts': posts, 'topics': topics,
               'post_count': post_count, 'post_messages': post_messages}
    return render(request, 'base/home.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    post_messages = post.message_set.all()
    participants = post.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            post=post,
            body=request.POST.get('body')
        )
        post.participants.add(request.user)
        return redirect('post', pk=post.id)

    context = {'post': post, 'post_messages': post_messages,
               'participants': participants}
    return render(request, 'base/post.html', context)


@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Post.objects.create(
            host=request.user,
            topic=topic,
            description=request.POST.get('description'),
            photo=request.FILES['photo'],
        )

        return redirect('home')

    context = {'form': form, 'topics': topics}

    return render(request, 'base/post_form.html', context)


@login_required(login_url='login')
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    topics = Topic.objects.all()

    if request.method == 'POST':
        form = PostForm(instance=post)
        if form.is_valid():
            topic_name = request.POST.get('topic')
            topic, created = Topic.objects.get_or_create(name=topic_name)
            post.description = request.POST.get('description')
            post.topic = topic
            post.photo = request.POST.get('photo')
            post.save()
            context = {'form': form, 'topics': topics, 'post': post}

            return render(request, 'base/update_post.html', context)

    context = {'form': form, 'topics': topics, 'post': post}
    return render(request, 'base/post_form.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST' and request.user == post.host:
        post.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': post})


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('home')


@login_required(login_url='login')
def delete_message(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})


def topics_page(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})


def activity_page(request):
    post_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'post_messages': post_messages})


