# configurar el patron de la url
from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea

# La url sace que mostrara el contenido de la vista
# Tomara en cuenta el template donde este configurado
urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'),
               # Locaso solo con mandar el id automaticamente lo toma y retorna el objeto
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')]

# Basicamnet elas rutas las busca el sistema de manera automatica, las podemos rebautizar.
# pero tenemos en cuenta principalamente el nombre del modelo alinicio de ahi los isgnos especiales
