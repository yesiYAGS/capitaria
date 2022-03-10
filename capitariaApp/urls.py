from django.urls import path
from capitariaApp import views

urlpatterns = [
    path('', views.inicio),
    path('colegio', views.colegio),
    path('agenda',views.agenda),
]