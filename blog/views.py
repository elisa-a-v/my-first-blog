from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

def post_list(request):
    user = User.objects.all()
    misposts = Post.objects.all()
    arguments = {'posts': misposts, 'mi_usuario': user}
    return render(request, 'blog/post_list.html', arguments)