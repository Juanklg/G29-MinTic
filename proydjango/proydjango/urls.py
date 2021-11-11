from django.contrib import admin
from django.urls import path,include
from proydjango.views import *
from gestor.views import *

urlpatterns = [
    path('', videos,name='home'),
    path('admin/', admin.site.urls),
    path('fecha/', fecha),
    path('calculo/<int:fechaNacimiento>/<int:fechaFutura>', calculo),
    path('tareas/', tareas),

    path('login/', usuarioLogin,name='login'),
    path('signin/', usuarioAdd,name='signin'),
    path('logout/', usuarioLogout,name='logout'),
    # gestor
    path('gestor/', include('gestor.urls'))#,{'blog_id': 3}
]
