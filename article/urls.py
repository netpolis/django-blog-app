from django.contrib import admin
from django.urls import path

from . import views

app_name="article"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"), 
    path('addarticle/',views.addarticle,name="addarticle"), 
    path('delete/<int:id>',views.deleteArticle,name="deleteArticle"), 
    path('article/<int:id>',views.detailArticle,name="detailArticle"),
    path('update/<int:id>',views.updateArticle,name="updateArticle"), 
    path('',views.articles,name="articles"), 
    path('addComment/<int:id>',views.addComment,name="addComment"), 



    
]