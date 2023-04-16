from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# Para contruir nuestra clase de registro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy  # enviar a un lugar especifico al suceder un evento
from .models import Tarea

#  Login
from django.contrib.auth.views import LoginView
# Restringe nuestras vistas
from django.contrib.auth.mixins import LoginRequiredMixin


class Logueo(LoginView):
    template_name = "base/login.html"
    # Usamos todos los camops
    field = '__all__'
    redirect_field_name = True

    # Situo al que ira al usuario una vez se halla logeado
    def get_success_url(self):
        return reverse_lazy('tareas')

    # Create your views here.


class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_field_name = True
    success_url = reverse_lazy('tareas')

#! Para el logueo del usuario
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro, self).get(*args, **kwargs)
# La lista tendra una lista de objetos
class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    # nombre del contexto
    context_object_name = "tareas"

    # se le pasara argumetnos clave
    # Se busca solo lo que halla ingresado las tareas un usuario
    def get_context_data(self, **kwargs):
        # informacion agregada a la data
        contex = super().get_context_data(**kwargs)
        contex['tareas'] = contex['tareas'].filter(usuario=self.request.user)
        contex['count'] = contex['tareas'].filter(completo=False).count()

        return contex


class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = "tarea"
    template_name = 'base/tarea.html'


# Crear neuvos elementos en la lista

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    # fields = '__all__', ahora solo se mostaran algunos campos
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

    # sobreescritura del metodo de form vlues
    # La tarea que se realice por cada uusario se registrara de manera automatica
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    # los elementos queremos sean refderenciados como tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')
