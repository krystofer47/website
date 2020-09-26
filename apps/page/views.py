from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse
from urllib.parse import urlencode
from .forms import ContactForm
import requests
import math

from apps.post.models import Post, Tag
# Create your views here.

class HomeView(ListView):
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
        
        if self.p_filter != None:
            self.p_filter = self.p_filter.replace('%2C', ',')

        # Parse filter to ["A", "B", ...]
        if self.p_filter != None:
            self.p_filter = self.p_filter.split(sep=",")
            f_tags = Tag.objects.filter(name__in=self.p_filter)

        
        # set number_of_pages depending on if a filter exists or not
        if self.p_filter != None:

            # For multiple Filters
            querysets = []
            for tag in f_tags:
                querysets.append(Post.objects.filter(tags=tag))
            
            result = querysets[0]
            for queryset in querysets:
                result = result.intersection(queryset)

            self.n_pages = math.ceil(result.count() / 5)
        else:
            self.n_pages = math.ceil(Post.objects.all().count() / 5) 

        if self.n_pages == 0:
            self.n_pages = 1

        # if current page is <= 0 redirect to page = 1, with filter or without
        if page <= 0:
            if self.p_filter != None:
                base_url = reverse('page:page', kwargs = {'page': 1})
                query_string = urlencode({'filter': '%2C'.join(self.p_filter)})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
            return redirect('page:page', page = 1)

        # if current page is > number_of_pages redirect to page = number_of_pages, with filter or without
        if page > self.n_pages:
            if self.p_filter != None:
                base_url = reverse('page:page', kwargs = {'page': self.n_pages})
                query_string = urlencode({'filter': '%2C'.join(self.p_filter)})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
            return redirect('page:page', page = self.n_pages)

        # Set context depending of with or without filter, after redirect to reduce unnecassary load on db
        if self.p_filter != None:
            context['posts'] = result[(page - 1) * 5:page * 5] 
        else:
            context['posts'] = Post.objects.all()[(page - 1) * 5:page * 5]

        # filter_tags
        context['f_tags'] = f_tags
        # if filter_tags != None remove the filter_tags from the tags
        if f_tags != None:
            context['tags'] = Tag.objects.all().difference(f_tags)
            context['f_tags_str'] = ','.join(self.p_filter)
        else:
            context['tags'] = Tag.objects.all()
        context['page'] = page
        context['in_home'] = True # For Header
        return render(request, self.template_name, context=context)
    
class AboutView(TemplateView):
    template_name = "page/about.html"
    repos = []

    # Override setup to fetch all necessary information from github here
    def setup(self, request, *args, **kwargs):
        super().setup(request)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["in_about"] = True # For Header
        return context

class ContactView(FormView):
    template_name = "page/contact.html"
    form_class = ContactForm
    success_url = '/contact/?sent=True'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["in_contact"] = True # For Header
        if self.request.GET.get('sent', False):
            context['sent'] = True 
        return context
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class PrivacyView(TemplateView):
    template_name="page/privacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context