from django.urls import path,re_path
from django.contrib.auth.decorators import login_required
#from .views import ListarClientes,EliminarClientes,EditarClientes,CrearClientes,Usuarios_tramites,buscar_clientes,CrearModalClientes
from .views import EliminarTramites,EditarTramites,CrearTramites,buscar_tramites,CrearModalTramites
from .views import EliminarClientes_Tramites,EditarClientes_Tramites,CrearClientes_Tramites,buscar_clientes_tramites,CrearModalClientes_Tramites,buscar_clientes_tramites_fechas,buscar_usuarios_tramites
from .views import EliminarCedulas,EditarCedulas,CrearCedulas,buscar_cedulas,CrearModalCedulas,buscar_cedulas_fechas,buscar_usuarios_cedulas
from .views import CrearCasilleros, buscar_casilleros, EditarCasilleros, EliminarCasilleros,CrearModalCasilleros



urlpatterns = [


    path('crear_tramites/', login_required(CrearTramites.as_view()), name = 'crear_tramites'),
    path('crear__tramites/', login_required(CrearModalTramites.as_view()), name = 'crear__tramites'),
    path('listar_tramites/', login_required(buscar_tramites), name = 'listar_tramites'),
    path('editar_tramites/<int:pk>', login_required(EditarTramites.as_view()), name = 'editar_tramites'),
    path('eliminar_tramites/<int:pk>',login_required(EliminarTramites.as_view()), name = 'eliminar_tramites'),

    path('crear_casilleros/', login_required(CrearCasilleros.as_view()), name = 'crear_casilleros'),
    path('crear__casilleros/', login_required(CrearModalCasilleros.as_view()), name = 'crear__casilleros'),
    path('listar_casilleros/', login_required(buscar_casilleros), name = 'listar_casilleros'),
    path('editar_casilleros/<int:pk>', login_required(EditarCasilleros.as_view()), name = 'editar_casilleros'),
    path('eliminar_casilleros/<int:pk>',login_required(EliminarCasilleros.as_view()), name = 'eliminar_casilleros'),

    path('crear_clientes_tramites/', login_required(CrearClientes_Tramites.as_view()), name = 'crear_clientes_tramites'),
    path('crear__clientes_tramites/', login_required(CrearModalClientes_Tramites.as_view()), name = 'crear__clientes_tramites'),
    path('listar_clientes_tramites/', login_required(buscar_clientes_tramites), name = 'listar_clientes_tramites'),
    path('listar_usuarios_tramites/', login_required(buscar_usuarios_tramites), name='listar_usuarios_tramites'),
    path('listar_clientes_tramites_busqueda/', login_required(buscar_clientes_tramites_fechas), name = 'listar_clientes_tramites_busqueda'),
    path('editar_clientes_tramites/<int:pk>', login_required(EditarClientes_Tramites.as_view()), name = 'editar_clientes_tramites'),
    path('eliminar_clientes_tramites/<int:pk>',login_required(EliminarClientes_Tramites.as_view()), name = 'eliminar_clientes_tramites'),
    #path('buscar_clientes_tramites/', login_required(listar_busqueda), name = 'buscar_clientes_tramites'),
   
    path('crear_cedulas/', login_required(CrearCedulas.as_view()), name = 'crear_cedulas'),
    path('crear__cedulas/', login_required(CrearModalCedulas.as_view()), name = 'crear__cedulas'),
    path('listar_cedulas/', login_required(buscar_cedulas), name = 'listar_cedulas'),
    path('listar_usuarios_cedulas/', login_required(buscar_usuarios_cedulas), name='listar_usuarios_cedulas'),
    path('listar_cedulas_busqueda/', login_required(buscar_cedulas_fechas), name = 'listar_cedulas_busqueda'),
    path('editar_cedulas/<int:pk>', login_required(EditarCedulas.as_view()), name = 'editar_cedulas'),
    path('eliminar_cedulas/<int:pk>',login_required(EliminarCedulas.as_view()), name = 'eliminar_cedulas'),



    #re_path(r'^crear_clientes/(?P<id>\d+)',crearClientes, name ="")
    ]

"""
    path('crear_clientes/', login_required(CrearClientes.as_view()), name = 'crear_clientes'),
    path('crear__clientes/', login_required(CrearModalClientes.as_view()), name = 'crear__clientes'),
    path('listar_clientes/', login_required(buscar_clientes), name = 'listar_clientes'),
    path('editar_clientes/<int:pk>', login_required(EditarClientes.as_view()), name = 'editar_clientes'),
    path('eliminar_clientes/<int:pk>',login_required(EliminarClientes.as_view()), name = 'eliminar_clientes'),

"""