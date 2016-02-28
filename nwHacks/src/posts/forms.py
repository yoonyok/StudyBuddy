from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Post
        fields = [
            'title',
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
