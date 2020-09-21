from django.shortcuts import render
from django.views import generic

from apps.post.models import Post
# Create your views here.

class HomeView(generic.ListView):
    model = Post
    template_name = 'page/home.html'
    context_object_name = 'post_list'
    queryset = Post.objects.all()
