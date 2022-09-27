from distutils.command.upload import upload
from unicodedata import name
from django.contrib.auth.models import User
from pickle import TRUE
from tabnanny import verbose
from django.db import models
from user.models import *



class Kategori(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "kategori"
        
class Input(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True, related_name='berkas_user')
    body = models.TextField(max_length=200, blank=False, null= False)
    image = models.FileField(upload_to='fileInput')
    date= models.DateTimeField(auto_now_add=True)
    kategory = models.ForeignKey(Kategori, on_delete=models.PROTECT)
    def __str__(self):
        return self.body
    
    class Meta:
       ordering = ['-id']
       verbose_name_plural = "Input"
       




    