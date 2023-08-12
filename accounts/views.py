from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages


User = get_user_model()


def login(request):
    form =LoginForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you are logged in!')
            return redirect('/')
        else:
            messages.error(request, 'invalid login')
    return render(request, 'accounts/login.html', context)





