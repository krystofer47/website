from django.shortcuts import render
from django.views.generic import detail
from .models import Post

# Create your views here.

class PostDetailView(detail.DetailView):
    template_name = "post/detail.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

