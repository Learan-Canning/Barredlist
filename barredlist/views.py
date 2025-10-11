from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from requests import post
from .models import Post, Comment, Reaction 
from .forms import CommentForm, ReactionForm


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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    # Get reaction counts
    reaction_counts = {}
    from .models import REACTION_TYPES
    for reaction_type, label in REACTION_TYPES:
        count = post.reactions.filter(reaction_type=reaction_type).count()
        reaction_counts[label] = count
    
    # Check if user has already reacted
    user_reaction = None
    if request.user.is_authenticated:
        try:
            user_reaction = Reaction.objects.get(post=post, user=request.user)
        except Reaction.DoesNotExist:
            user_reaction = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():  # This needs to be indented under the POST check
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    
    comment_form = CommentForm()  # Create empty form for GET requests
    reaction_form = ReactionForm()

    return render(
        request,
        "barredlist/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "reaction_form": reaction_form,
            "reaction_counts": reaction_counts,
            "user_reaction": user_reaction,
        }
    )
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def post_reaction(request, slug):
    """
    Add or update a reaction to a post
    """
    if request.method == "POST" and request.user.is_authenticated:
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        reaction_form = ReactionForm(data=request.POST)
        
        if reaction_form.is_valid():
            reaction_type = reaction_form.cleaned_data['reaction_type']
            
            # Check if user already has a reaction for this post
            try:
                existing_reaction = Reaction.objects.get(post=post, user=request.user)
                existing_reaction.reaction_type = reaction_type
                existing_reaction.save()
                messages.add_message(request, messages.SUCCESS, 'Reaction updated!')
            except Reaction.DoesNotExist:
                # Create new reaction
                reaction = reaction_form.save(commit=False)
                reaction.post = post
                reaction.user = request.user
                reaction.save()
                messages.add_message(request, messages.SUCCESS, 'Reaction added!')
        else:
            messages.add_message(request, messages.ERROR, 'Error adding reaction!')
    
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
