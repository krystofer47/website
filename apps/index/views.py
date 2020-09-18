from django.shortcuts import render
from django.views import generic

from apps.post.models import Post
# Create your views here.

class IndexView(generic.ListView):
    model = Post
    template_name = 'index/index.html'
    context_object_name = 'post_list'
    queryset = Post.objects.all()
