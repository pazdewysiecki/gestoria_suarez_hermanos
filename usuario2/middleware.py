from urllib import response
from tramites.models import Cedulas1, Clientes_Tramites

class PruebaMiddleware:
    
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.user.is_authenticated:
            clientes_tramites_usuarios = Clientes_Tramites.objects.filter(usuario = request.user)
            for clientes_tramites_usuario in clientes_tramites_usuarios:
                clientes_tramites_usuario.save()

    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.user.is_authenticated:
            cedulas_usuarios = Cedulas1.objects.filter(usuario = request.user)
            for cedulas_usuario in cedulas_usuarios:
                cedulas_usuario.save()
