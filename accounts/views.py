from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, GuestForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from .models import GuestEmail



User = get_user_model()



def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {'form':form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data['email']
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        print(url_has_allowed_host_and_scheme(redirect_path, request.get_host()))
        if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/register/')
    return redirect('/register/')


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
            try:
                del request.session['guest_email_id']
            except:
                pass
            if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            messages.error(request, 'invalid login')
    return render(request, 'accounts/login.html', context)





