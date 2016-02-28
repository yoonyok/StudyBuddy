from django import forms
from .models import Post
from django.contrib.admin import widgets
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'course',
            'content',
            'phone_number',
            'start_time',
            'end_time',
            'address',
            'city',
            'postal_code',
        ]

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']

