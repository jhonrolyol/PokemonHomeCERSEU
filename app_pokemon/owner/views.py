from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from owner.models import Owner
def list_owner(request):

    # data_context = {
    #     'nombre': 'Jesús de La Cruz',
    #     'edad': 29,
    #     'pais_nacimiento':'Peru',
    #     'dni': '951456123',
    #     'vigente': False
    # }

    data_context = [
        {
            'nombre': 'Jesús de La Cruz',
            'edad': 26,
            'pais_nacimiento': 'Peru',
            'dni': '451456653',
            'vigente': True,
            'pokemons':[
                {
                    'nombre_pokemon': 'Charizard',
                    'ataques': ['Ataque 1 - Charizard', 'Ataque 2 - Charizard', 'Ataque 3 - Charizard']
                }
            ]
        },
        {
            'nombre': 'Eduardo Gutierrez',
            'edad': 28,
            'pais_nacimiento': 'Brasil',
            'dni': '4651456123',
            'vigente': True,
            'pokemons': []
        },
        {
            'nombre': 'Maria Luiza',
            'edad': 35,
            'pais_nacimiento': 'México',
            'dni': '4123456123',
            'vigente': True,
            'pokemons': []
        }
    ]

    """Crear un objeto en una tabla de la BD"""
    # p = Owner(nombre="Juliana", pais="España", edad=26)
    # p.save()  # Guarda el registro en la B.D.

    # p.nombre = "Samanta"
    # p.save()

    """Obtener todos los elementos de una tabla de la BD"""
    # owners = Owner.objects.all()

    """Filtración de datos: .filter()"""
    # owners = Owner.objects.filter(nombre="Paolo")

    """Filtración de datos con AND de SQL: filter()"""
    # owners = Owner.objects.filter(nombre="Juliana", edad=26)

    """Filtración de datos más precisos con : __contains"""
    # owners = Owner.objects.filter(nombre__contains="Benito")

    """Filtración de datos más precisos con: __endswith"""
    # owners = Owner.objects.filter(nombre__endswith="ima")

    """Obtener un solo objeto de la tabla en la BD"""
    # owners = Owner.objects.get(dni="63451234")

    # print("El dato es: {}".format(owners))
    # print("Tipo de datos: {}".format(type(owners)))

    """Ordenar por cualquier atributo o campo de la tabla"""

    """Ordenar alfabéticamente por nombre"""
    # owners = Owner.objects.order_by('-edad')

    """Ordenar concatenando diferentes métodos de ORMs"""
    # owners = Owner.objects.filter(nombre="Juliana").order_by("-edad")

    """Acortar datos: Obtener un rango de registro de una talba en la BD"""
    owners = Owner.objects.all()[0:5]

    """Eliminando un conjunto de datos es específico"""
    owners = Owner.objects.filter(id=3)
    owners.delete()
    return render(request, 'owner/owner_list.html', context={'data':owners})
