
from django.contrib.auth import login
from django.shortcuts import redirect, render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

import article

# Create your views here.

def articles(request):
    articles=Article.objects.all()        
    
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})

    return render(request,"articles.html",{"articles":articles})


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


@login_required(login_url = "user:login" )
def dashboard(request):
    articles=Article.objects.filter(author=request.user)    

    return render(request,"dashboard.html",{"articles":articles})


def deleteArticle(request,id):
    article=Article.objects.filter(id=id).first()
    article.delete()
    messages.success(request,"Makale Sileme işlemi başarılır")
    return redirect("article:dashboard")


def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)    
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makale başarı ile güncellendi")
        return redirect(f"/articles/article/{article.id}")


    return render(request,"updateArticle.html",{"form":form})

  
@login_required(login_url = "user:login" )
def addarticle(request):

    
    form=ArticleForm(request.POST or None,request.FILES or None)
    print(request.FILES)

    if form.is_valid():
        """
        article=form.save(commit=False)
        from.save() işlemi gelen bilgilerden önce bir article nesnesi oluşturur 
        ve ardından bu nesneyi kayıt eder. burada araya giremediğimiz için hata alırız.
        çünkü zorunlu alnlardan author bilgisi yok.
        Bunun için 
        article=form.save(commit=False) şeklinde kayıt önlenir ve 
        article nesnesine author bilgisi girildikten sonra kayıt işlemi gerçekleştirilir.
        """
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makale Başarı ile kayıt edildi")
        return redirect("article:dashboard")



    return render(request,"addarticle.html",{"form":form})


def detailArticle(request,id):
    #article=Article.objects.filter(id=id).first() 
    article=get_object_or_404(Article,id=id)

    comments=article.commands.all()
    

    return render(request,"detailArticle.html",{"article":article,"comments":comments})

def addComment(request,id):
    article=get_object_or_404(Article,id=id)

    if request.method=="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()

    return redirect(reverse("article:detailArticle",kwargs={"id":id}))










