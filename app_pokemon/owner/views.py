from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_owner(request):

    data_context = {
        'nombre': 'Jesús de La Cruz',
        'edad': 29,
        'pais_nacimiento':'Peru',
        'dni': '951456123',
        'vigente': False
    }

    data_context = [
        {
            'nombre': 'Jesús de La Cruz',
            'edad': 26,
            'pais_nacimiento': 'Peru',
            'dni': '451456653',
            'vigente': True
        },
        {
            'nombre': 'Eduardo Gutierrez',
            'edad': 28,
            'pais_nacimiento': 'Brasil',
            'dni': '4651456123',
            'vigente': True
        },
        {
            'nombre': 'Maria Luiza',
            'edad': 35,
            'pais_nacimiento': 'México',
            'dni': '4123456123',
            'vigente': True
        }
    ]

    return render(request, 'owner/owner_list.html', context={'data':data_context})
