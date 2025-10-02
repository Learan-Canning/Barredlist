from django import forms
from .models import Comment, Reaction

# ...existing code...

class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ['reaction_type']
        widgets = {
            'reaction_type': forms.RadioSelect(),
        }