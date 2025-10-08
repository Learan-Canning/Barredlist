from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "barredlist/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`barredlist.Post`.

    **Context**

    ``post``
        An instance of :model:`barredlist.Post`.

    **Template:**

    :template:`barredlist/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "barredlist/post_detail.html",
        {"post": post},
    )