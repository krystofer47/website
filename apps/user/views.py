from django.shortcuts import render, redirect
from django.views import generic

from django.contrib.auth.models import User
from .models import Profile
from apps.post.models import Post

# Create your views here.

class ProfilView(generic.TemplateView):
    template_name = "user/profile.html"

    def get_context_data(self, **kwargs):
         user = kwargs.get('user')
         context = super().get_context_data(**kwargs)
         context['user'] =  Profile.objects.get(user = User.objects.get(username = user))
         context['posts'] = Post.objects.filter(author = User.objects.get(username = user))
         return context