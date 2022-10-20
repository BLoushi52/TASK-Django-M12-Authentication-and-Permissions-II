from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import UserRegister
from django.contrib.auth import login


def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            # Where you want to go after a successful signup
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)