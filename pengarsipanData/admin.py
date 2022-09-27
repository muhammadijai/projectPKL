from django.contrib import admin
from dokumen .models import *


class fileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Input, fileAdmin)

admin.site.register(Kategori)
