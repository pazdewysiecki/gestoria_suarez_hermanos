from django.contrib import admin
from .models import *
#from import_export import resources
#from import_export.admin import ImportExportModelAdmin
# Register your models here.

from .models import Tramites,Clientes_Tramites, Casilleros3, Cedulas1


#class ClientesResource(resources.ModelResource):
 #   class Meta:
  #      model = Clientes



"""
class ClientesAdmin(admin.ModelAdmin):
    search_fields = ['nombre_cliente']
    list_display = ('nombre_cliente','telefono_cliente','mail_cliente',)
    #resource_class = ClientesResource
"""

class Clientes_TramitesAdmin(admin.ModelAdmin):
    search_fields = ['id','autos']
    list_display = ('id','tramite_id','autos','estado_tramite_iniciado','estado_tramite_finalizado','estado_tramite_anulado','comentarios_tramite','fecha_creacion')

class TramitesAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre_tramite','descripcion_tramite']
    list_display = ('id','nombre_tramite', 'descripcion_tramite',)



class CedulasAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id')

class CasillerosAdmin(admin.ModelAdmin):
    search_fields = ['casillero']
    list_display = ('casillero')




admin.site.register(Tramites,TramitesAdmin)
#admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Clientes_Tramites,Clientes_TramitesAdmin)

#admin.site.register (Post)