from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "barredlist/index.html"
    paginate_by = 6