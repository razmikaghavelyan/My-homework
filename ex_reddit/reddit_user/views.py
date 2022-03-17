from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from reddit_user.forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_register(request):
    user_form = UserCreationForm()
    if request.method == "POST":
        print(request.POST)
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        messages.success(request, "User create successfully")
    context = {"form": user_form}

    return render(request, "reddit_user/home.html", context)


def user_login(request):
    user_login_form = UserLoginForm()

    if request.method == "POST":
        user_login_form = UserLoginForm(request.POST)

        if user_login_form.is_valid():
            username = user_login_form.cleaned_data["username"]
            password = user_login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            # if user:
            #     login(request, user)
            #
            #     return redirect("list_task")
            #     messages.success(request, "Welcome back")
        messages.warning(request, "Wrong password or login")

    context = {"form": user_login_form}

    return render(request, "reddit_user/user_login.html", context)


def user_logout(request):
    logout(request)
    messages.success(request, "Hope you come back")
    return redirect('list_task')
