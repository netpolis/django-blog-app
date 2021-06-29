from django import forms
from django.forms import fields
from django.forms.models import fields_for_model
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=["title","content","article_images"]


    
    