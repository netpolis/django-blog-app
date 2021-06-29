
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=50,verbose_name="Başlık")
    content=RichTextField(verbose_name="İçerik")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_images=models.FileField(blank=True,null=True,verbose_name="Bir resim yükleyin")

    def __str__(self):
        return self.title

    class Meta:
        ordering=["-created_date"]

   
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=CASCADE,related_name="commands",verbose_name="Makale")    
    comment_author=models.CharField(max_length=50, verbose_name="İsim")
    comment_content=models.CharField(max_length=500, verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True,verbose_name="Tarih")
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering=["-comment_date"]
