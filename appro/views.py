from django.http.response import HttpResponse
from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    tache_list=Tache.objects.all()
    contex={
        'tache_list':tache_list
    }
    return render(request,'index.html',contex)
   
def add_tache(request):
    if request.method=="POST":
        date=request.POST['date']
        object=request.POST['object']
        description=request.POST['description']
        tache=Tache(date=date,object=object,description=description)
        tache.save()
        messages.info(request,"La tache ajoute avec succes")

    else:
        pass
    tache_list=Tache.objects.all()
    contex={
        'tache_list':tache_list
    }
    return render(request,'index.html',contex)

def delete_tache(request,myid):
    tache=Tache.objects.get(id=myid)
    tache.delete()
    messages.info(request,"La tache supprimee avec succes")

    return redirect(index)

def edit_tache(request,myid):
    sel_tache=Tache.objects.get(id=myid)
    tache_list=Tache.objects.all()
    context={
        'sel_tache':sel_tache,
        'tache_list':tache_list

    }

    return render(request,'index.html',context)

def update_tache(request,myid):
    tache=Tache.objects.get(id=myid)
    tache.date=request.POST['date']
    tache.object=request.POST['object']
    tache.description=request.POST['description']
    tache.save()
    messages.info(request,"Votre tache est modifier avec succes")

    return redirect(request,'index.html')
