from django import forms
from .models import Comment, Reaction 


# ...existing code...

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ['reaction_type']
        widgets = {
            'reaction_type': forms.RadioSelect(),
        }

