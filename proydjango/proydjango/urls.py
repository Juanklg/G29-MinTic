from django.contrib import admin
from django.urls import path,include
from proydjango.views import *

urlpatterns = [
    path('', saludar),
    path('admin/', admin.site.urls),
    path('fecha/', fecha),
    path('calculo/<int:fechaNacimiento>/<int:fechaFutura>', calculo),
    path('tareas/', tareas),
    path('videos/', videos),
    
    path('gestor/', include('gestor.urls'))#,{'blog_id': 3}
]
