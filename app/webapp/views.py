from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Professor! Sou seu aluno Miguel Rodrigues Spínola da Hora em SO!")