# configurar el patron de la url
from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea

# La url sace que mostrara el contenido de la vista
# Tomara en cuenta el template donde este configurado
urlpatterns = [path('', ListaPendientes.as_view(), name='pendientes'),
               # Locaso solo con mandar el id automaticamente lo toma y retorna el objeto
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea')]
