from django.contrib import admin

# Register your models here.
from . models import *

class BiodataAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'alamat', 'jabatan','telp')
admin.site.register(Biodata, BiodataAdmin)


