from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from user.forms import UserLoginForm


def user_register(request):
    user_form = ""
    if request.method == "GET":
        user_form = UserCreationForm()
    elif request.method == "POST":
        print(request.POST)
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

    context = {"form": user_form}

    return render(request, "user/home.html", context)


def user_login(request):
    user_login_form = UserLoginForm()

    if request.method == "POST":
        user_login_form = UserLoginForm(request.POST)

        if user_login_form.is_valid():
            username = user_login_form.cleaned_data["username"]
            password = user_login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

                return redirect("list_task")

    context = {"form": user_login_form}

    return render(request, "user/user_login.html", context)


def user_log_out(request):
    logout(request)

    return redirect("user_login")