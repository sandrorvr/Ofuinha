from django.shortcuts import render
from blog.models import Posts, PostDetail

def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'home.html', context)

def article(request, art):
    context = {
        'detail': PostDetail.objects.get(id=art)
    }
    return render(request, 'article.html', context)