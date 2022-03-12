from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def inicio (request):
    return render (request,'inicio.html')

def colegio(request):
    return render(request,'colegio.html')

def agenda(request):
    return render(request,'agenda.html')
def agenda2(request):
    context = {
        "data": {
                "LUNES": [
                    {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
                    {"name": "Jorge", "start_time": "09:30", "end_time": "11:00"},
                    {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
                    {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
                ],
                "MARTES": [
                    {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
                    {"name": "Jorge", "start_time": "11:30", "end_time": "12:00"},
                    {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
                    {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
                ],
                "MIERCOLES": [
                    {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
                    {"name": "Jorge", "start_time": "10:30", "end_time": "12:00"},
                    {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
                    {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
                ],
                "JUEVES": [
                    {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
                    {"name": "Jorge", "start_time": "09:30", "end_time": "12:00"},
                    {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
                    {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
                ],
                "VIERNES": [
                    {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
                    {"name": "Jorge", "start_time": "09:30", "end_time": "12:00"},
                    {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
                    {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
                ],
                "SABADO": [
                    {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
                    {"name": "Jorge", "start_time": "09:30", "end_time": "12:00"},
                    {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
                    {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
                ],
                "DOMINGO": [
                    {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
                    {"name": "Jorge", "start_time": "09:30", "end_time": "12:00"},
                    {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
                    {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
                ],
            }
    }
    return JsonResponse(context)
def agenda3(request):
    return render(request,'agenda3.html')

# Create your views here.
