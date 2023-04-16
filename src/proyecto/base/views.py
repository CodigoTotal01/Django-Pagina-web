from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy  # enviar a un lugar especifico al suceder un evento

from .models import Tarea


# Create your views here.


# La lista tendra una lista de objetos
class ListaPendientes(ListView):
    model = Tarea
    # nombre del contexto
    context_object_name = "tareas"


class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = "tarea"
    template_name = 'base/tarea.html'


# Crear neuvos elementos en la lista

class CrearTarea(CreateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')
