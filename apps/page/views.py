from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from urllib.parse import urlencode
import math

from apps.post.models import Post, Tag
# Create your views here.

class HomeView(generic.ListView):
    n_pages = math.ceil(Post.objects.all().count() / 5) 
    model = Post
    template_name = 'page/home.html'
    p_filter = None
    
    def get(self, request, page = 1):
        
        context = {}
        f_tags = None

        # Get filter from request, defaults to None
        self.p_filter = request.GET.get('filter', None)
        if self.p_filter == '':
            self.p_filter = None

        # Parse filter to ["A", "B", ...]
        if self.p_filter != None:
            self.p_filter = self.p_filter.split(sep=",")
            f_tags = Tag.objects.filter(name__in=self.p_filter)

        # set number_of_pages depending on if a filter exists or not
        if self.p_filter != None:
            self.n_pages = math.ceil(Post.objects.filter(tags__in=f_tags).count() / 5)
        else:
            self.n_pages = math.ceil(Post.objects.all().count() / 5) 

        # if current page is <= 0 redirect to page = 1, with filter or without
        if page <= 0:
            if self.p_filter != None:
                base_url = reverse('page:page', kwargs = {'page': 1})
                query_string = urlencode({'filter': self.p_filter[0]})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
            return redirect('page:page', page = 1)

        # if current page is > number_of_pages redirect to page = number_of_pages, with filter or without
        if page > self.n_pages:
            if self.p_filter != None:
                base_url = reverse('page:page', kwargs = {'page': self.n_pages})
                query_string = urlencode({'filter': self.p_filter[0]})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
            return redirect('page:page', page = self.n_pages)

        # Set context depending of with or without filter, after redirect to reduce unnecassary load on db
        if self.p_filter != None:
            context['posts'] = Post.objects.filter(tags__in=f_tags)[(page - 1) * 5:page * 5] 
        else:
            context['posts'] = Post.objects.all()[(page - 1) * 5:page * 5]

        # filter_tags
        context['f_tags'] = f_tags
        # if filter_tags != None remove the filter_tags from the tags
        if f_tags != None:
            context['tags'] = Tag.objects.all().difference(f_tags)
        else:
            context['tags'] = Tag.objects.all()
        context['page'] = page

        return render(request, self.template_name, context=context)