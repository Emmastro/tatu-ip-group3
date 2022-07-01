from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def aboutUs(request):
    return render(request, 'about_us.html')

def posts(request):
    return render(request, 'posts.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')
