from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_owner(request):
    print("Probando vista!! ")
    name = "CERSEU"
    return HttpResponse(name)
