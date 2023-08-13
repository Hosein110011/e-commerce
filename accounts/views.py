from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme


User = get_user_model()



def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        new_user = User.objects.create_user(username, email, password)
    return render(request, 'accounts/register.html', context)


def login_view(request):
    form =LoginForm(request.POST or None)
    context = {'form':form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            messages.error(request, 'invalid login')
    return render(request, 'accounts/login.html', context)





