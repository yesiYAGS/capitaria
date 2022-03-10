from django.shortcuts import render, redirect, HttpResponse

def inicio (request):
    return render (request,'inicio.html')

def colegio(request):
    return render(request,'colegio.html')

def agenda(request):
    return render(request,'agenda.html')

# Create your views here.
