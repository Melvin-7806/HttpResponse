from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def A(request):
    return HttpResponse('Hi this is Inshot App')
