from django import forms 

from .models import Comment, Opinion


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text')


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ('text',)
