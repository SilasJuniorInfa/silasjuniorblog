from os import error

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text']
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'text': 'Your Comment',}
        error_messages = {
            'user_name': {
                'required': 'Please enter your name.',
                'max_length': 'Name cannot exceed 120 characters.',
            },
            'user_email': {
                'required': 'Please enter your email address.',
                'invalid': 'Enter a valid email address.',
            },
            'text': {
                'required': 'Please enter your comment.',
                'max_length': 'Comment cannot exceed 400 characters.',
            },
        }
        
        