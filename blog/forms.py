from django import forms
from blog.models import Comment, Post


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {'content': forms.Textarea(attrs={'class': 'form-control'})}


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'places')

        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'content': forms.Textarea(attrs={'class': 'form-control'}),
                   'places': forms.SelectMultiple(attrs={'class': 'form-control'})}
