from django import forms
from .models import Post, Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
