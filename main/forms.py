from django import forms
from .models import *
from django.forms import ModelForm


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','media_file', 'caption','tags']
        labels = {
            'title': 'Title',
            'media_file': 'Upload File',
            'caption': 'Caption',
            'tags':'Category'
        }
        
        widgets = {
            'caption':forms.Textarea(attrs={'rows':4,'placeholder':'Go ahead, say anything...'}),
             'tags': forms.CheckboxSelectMultiple()
        }
        
class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'caption','tags']
        
        labels = {
            'title':'Title',
            'caption':'Caption',
            'tags':'Category'
        }
        widgets = {
            'caption':forms.Textarea(attrs={'rows':3,'placeholder':'Go ahead, say anything!'}),
            'tags': forms.CheckboxSelectMultiple()
        }


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        
        exclude = ['user']
        
        labels = {
            'image': 'Profile Image',
            'middlename': 'Middle Name',
            'lastname': 'Last Name',
        }
        
        widgets = {
         'bio': forms.Textarea(attrs={'rows':3}),
         'image': forms.FileInput(),
        }