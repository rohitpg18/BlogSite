
from django import forms
from django.forms import ModelForm, Textarea
from .models import Blog


class UpdateBlog(ModelForm):
    class Meta:
        model   = Blog 
        fields  = '__all__'
        widgets = {
            'body': Textarea(attrs={'cols':120,'rows':15}),
        }



