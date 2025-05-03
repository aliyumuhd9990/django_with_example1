from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
# the app name
app_name = 'pages'

# Create your views here.

# CBVc
class HomePageView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'post'

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/detail.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'pages/add_post.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'pages/edit_post.html'
    fields = ['title', 'body']
    context_object_name = 'post'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'pages/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('pages:home')




