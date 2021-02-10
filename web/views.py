from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()[:3]
    }
    return render(request, 'web/index.html', context)

def post(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'web/post.html', context)

class PostDetailView(DetailView):
    model = Post