"""pengarsipanData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atexit import register
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

from .views import *

#from pengarsipanData.views import home, menu, registrasi#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('register/', registrasi, name='registrasi'),
    path('menu/', menu, name='menu' ),
    path('logout/', logout_view, name='logout'),
    path('File/', tabelFile, name="tabelFile"),
    url(r'^download/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    path('User/', tabelUser, name="tabelUser"),
    path('File/Upload/', inputan, name='inputan'), #<int:file_id>
    path('User/profil-user/<str:username>', profil_user, name="profil_user"),
    path('File/Delete-file/<str:id>', deleteFile, name="deleteFile"),
    
]


urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
