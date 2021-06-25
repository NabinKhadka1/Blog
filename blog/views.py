from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.views.generic.edit import CreateView, DeleteView,UpdateView,DeleteView
from django.contrib.auth import urls


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = "post_new.html"

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title','body']
    template_name = "post_edit.html"
    success_url = '/'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = '/'


