from inspect import getfile
import os
from msilib.schema import File
from tkinter.tix import InputOnly
from urllib import request, response
from django.contrib.auth.models import User
#from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout


from django.contrib.auth import authenticate
#from numpy import emath
from django.db import transaction

from user.models import Biodata
from dokumen . models import *
from dokumen . forms import *

from multiprocessing import context
from re import template
from django.contrib.auth.hashers import make_password
#from media import handle_uploaded_file

from django.http import HttpResponse

#class homeView(TemplateView):
#    template_name = 'home.html'

def home(request):
    if request.user.is_authenticated:
        print('sudah login')
        return redirect('menu')
    template_name = 'front/home.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            #data ada
            print('username benar')
            auth_login(request, user)
            return redirect('menu')
            
        else:
            #data tidak ada
            print('username salah')
    context = {
        'title' : 'form login'
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')

def registrasi(request):
    template_name = 'front/register.html'
    if request.method == "POST":
        username = request.POST.get('username')
        namadepan = request.POST.get('namadepan')
        namabelakang = request.POST.get('namabelakang')
        jabatan = request.POST.get('jabatan')
        email = request.POST.get('email')
        password = request.POST.get('password')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')
        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = namadepan,
                    last_name = namabelakang,
                    email = email
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    email = email,
                    jabatan = jabatan,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect(home)
        except:pass
        
    context = {
        'title':'form registrasi'
    }
    return render(request, template_name, context)

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
def menu(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'
    template_name = "back/dashboard.html"
    context = {
        'title': 'kolom menu',
    }
    return render(request, template_name, context)

@login_required
def tabelFile(request):
    template_name = "back/tabelFile.html"
    
    file=Input.objects.filter(name= request.user)
    #for a in file:
     #   print(a.name,'-',a.body)
    context = {
        'title' : 'Kolom Tabel File',
        'file': file,
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def tabelUser(request):
    template_name = "back/tabelUser.html"
    list_biodata = Biodata.objects.all()
    semua_user = User.objects.all()
    context = {
        'title' : 'Kolom Tabel User',
        'list_biodata':list_biodata,
        'semua_user' : semua_user,
        
    }
    return render(request, template_name, context)

def inputan(request,): #file_id
    template_name = "back/fileInput.html"
    if request.method == "POST": 
        forms_input = InputForms(request.POST, request.FILES) 
        if forms_input.is_valid():
            inp = forms_input.save(commit=False)
            inp.name = request.user
            inp.save()
            return redirect(tabelFile)
    else:
        forms_input = InputForms()
    context={
        'title' : 'Tambahkan File',
        'input' : input,
        'forms_input' : forms_input,
    }
    #file = Input.objects.get(pk=file_id)
    #if file is not None:
    return render(request, template_name, context) # {'file':file}
    #else:
     #   raise Http404(' ')
     
def profil_user(request, username):
    template_name="back/profil.html"
    ambil_user = User.objects.get(username=username)
    context = {
        'title' : 'lihat profil',
        # 'profil' : username,
        'ambil_user' : ambil_user,

    }
    return render(request, template_name, context)


def deleteFile(request, id):
    Input.objects.get(id=id).delete()
    return redirect(tabelFile)
     

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/image")
            response['content-disposition']='inline;filename='+os.path.basename(file_path)
            return response
        
        raise Http404

#def inputan(request,): #file_id
 #   template_name = "back/fileInput.html"
 #   if request.method == "POST": 
 #       forms_input = InputForms(request.POST, request.FILES) 
 #       files = request.FILES.getlist('image')
 #       if forms_input.is_valid():
 #           inp = forms_input.save(commit=False)
 #           inp.name = request.user
 #           category_obj = Kategori.objects.create(name=name)
 #           inp.save()
 #           if files:#check if user has uploaded some files
 #               for f in files:
 #                   Input.objects.create(image=f)
 #                   print(f)