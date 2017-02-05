# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:51:01 2017

@author: cheryl
"""

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)