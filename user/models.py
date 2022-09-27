from pickle import FALSE, TRUE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='biodata')
    email = models.CharField(max_length=50, null=TRUE)
    alamat = models.TextField(max_length=200, null=TRUE)
    jabatan = models.CharField(max_length=20, null=TRUE)
    telp = models.CharField(max_length=14)

    
    
    def __str__(self):
        return "{} - {}".format(self.user, self.telp)
    
    class Meta:
       ordering = ['-id']
    
