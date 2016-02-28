from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'course',
            'content',
            'preferred_location',
            'phone_number',
            'date',
            'start_time',
            'end_time',
            'address_number',
            'street_name',
            'postal_code',
            'city',
        ]

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']