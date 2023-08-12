from django.shortcuts import render
from .forms import ContactForm




def home_view(request):
    context = {"title":"Hello World!",
        "content":" Welcome to the homepage.",}
    if request.user.is_authenticated:
        context['premium_content'] = 'YEAHHHH'
    return render(request, 'home/home.html', context)


def about_view(request):
    context = {"title":"About Page",
        "content":" Welcome to the about page."}
    return render(request, 'home/about.html', context)


def contact_view(request):
    form = ContactForm(request.POST or None)
    context = {
         "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": form
    }
    if form.is_valid():
        pass
    
    
    return render(request, 'home/contact.html', context)
    

    