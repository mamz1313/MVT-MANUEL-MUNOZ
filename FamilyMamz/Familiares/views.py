from django.shortcuts import render
from .models import Familiar


# Create your views here.

def index(request):
    
    Graciela = Familiar(nombre='Graciela',edad=22,fecha='2000-02-17',parentesco='Esposa')
    Erika = Familiar(nombre='Erika',edad=54,fecha='1968-02-10',parentesco='Mamá')
    Fernando = Familiar(nombre='Fernando',edad=55,fecha='1967-01-31',parentesco='Papá')
    
    
    familia = [Graciela, Erika, Fernando]
    
    
    return render(request, 'index.html',{'lista':familia})
