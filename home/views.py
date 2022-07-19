from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def posts(request):
    return render(request, 'posts.html')

def authors(request):
    return render(request, 'authors.html')

def contact(request):
    return render(request, 'contact.html')

def background(request):
    return render(request, 'background.html')

def alu(request):
    return render(request, 'alu.html')
    
def mauritius(request):
    return render(request, 'mauritius.html')

def social(request):
    return render(request, 'social.html')

def career(request):
    return render(request, 'career.html')
    
def pictures(request):
    return render(request, 'pictures.html')

def comments(request):
    return render(request, 'comments.html')