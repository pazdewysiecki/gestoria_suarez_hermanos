from ast import Try
from http import client
from multiprocessing import context
from pydoc import cli
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView,ListView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 
from django.http import HttpResponse
from requests import request
from .forms import TramitesForm,Clientes_TramitesForm, CedulasForm, CasillerosForm
from .models import Casilleros3, Clientes_Tramites, Tramites, Cedulas1
from django.core.paginator import Paginator
from jsignature.utils import draw_signature
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError
from django import forms
from usuario2.models import Usuario
from django.contrib.auth.decorators import permission_required
from usuario2.mixins import ValidarPermisosRequeridosMixin


#Clase para inciar#

class Inicio(TemplateView):
    template_name = 'index.html'

class InicioSistema(TemplateView):
    template_name = 'home.html'

    """
    def home(request):
        queryset = request.GET.get("buscar")
        posts = Clientes_Tramites.objects.filter(Autos = 'autos' )
        if queryset:
            posts = Clientes_Tramites.objects.filter(
                Q( cliente_id__icontains = queryset) |
                Q( tramite_id__icontains = queryset) |
                Q( autos__icontains = queryset)
            ).distinct()
        return render(request, 'index.html', {'posts': posts})
"""

class Meta:
        ordering = ('date',)

        
#Clases para Clientes#
"""
class ListarClientes(ListView):
    model = Clientes
    template_name = 'tramites/listar_clientes.html'
    context_object_name = 'clientes'
    queryset = Clientes.objects.all()


class EditarClientes(UpdateView):
    model = Clientes
    template_name = 'tramites/modalclientes.html'
    form_class = ClientesForm
    success_url = reverse_lazy ('tramites:listar_clientes')


class CrearClientes(CreateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'tramites/crear_clientes.html'
    success_url = reverse_lazy ('tramites:listar_clientes')

class CrearModalClientes(CreateView):
    model = Clientes
    template_name = 'tramites/modalcrearclientes.html'
    form_class = ClientesForm
    success_url = reverse_lazy ('tramites:listar_clientes')

class EliminarClientes(DeleteView):
    model = Clientes
    success_url = reverse_lazy ('tramites:listar_clientes')


def buscar_clientes(request):
        busqueda = request.GET.get("buscar")
        clientes = Clientes.objects.all().order_by('-id')
        paginator = Paginator(clientes, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        if busqueda:
                clientes = Clientes.objects.filter(
                    Q (nombre_cliente__icontains = busqueda) |
                    Q (mail_cliente__icontains= busqueda) |
                    Q (id__icontains= busqueda)
                ).distinct()
                return render(request, 'tramites/listar_clientes.html', {'clientes':clientes})
        else:
            return render(request, 'tramites/listar_clientes.html', {'clientes': page_obj})

"""


#Clases para Tramites#

class ListarTramites(ValidarPermisosRequeridosMixin,ListView):
    model = Tramites
    template_name = 'tramites/listar_tramites.html'
    permission_required = ('tramites.view_tramites','tramites.add_tramites','tramites.delete_tramites','tramites.change_tramites')
    context_object_name = 'tramites'
    queryset = Tramites.objects.all()

@permission_required('tramites.view_tramites',login_url='home')
@permission_required('tramites.add_tramites',login_url='home')
@permission_required('tramites.delete_tramites',login_url='home')
@permission_required('tramites.change_tramites',login_url='home')
def buscar_tramites(request):
        busqueda = request.GET.get("buscar")
        tramites = Tramites.objects.all().order_by('-id')
        paginator = Paginator(tramites, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if busqueda:
            tramites = Tramites.objects.filter(
                Q (nombre_tramite__icontains = busqueda) |
                Q (id__icontains = busqueda)
            ).distinct()
            return render(request, 'tramites/listar_tramites.html', {'tramites':tramites})
        else:
            return render(request, 'tramites/listar_tramites.html', {'tramites': page_obj})


class EditarTramites(ValidarPermisosRequeridosMixin,UpdateView):
    model = Tramites
    template_name = 'tramites/modaltramites.html'
    permission_required = ('tramites.view_tramites','tramites.add_tramites','tramites.delete_tramites','tramites.change_tramites')
    form_class = TramitesForm
    success_url = reverse_lazy ('tramites:listar_tramites')

class CrearTramites(ValidarPermisosRequeridosMixin,CreateView):
    model = Tramites
    form_class = TramitesForm
    template_name = 'tramites/crear_tramites.html'
    permission_required = ('tramites.view_tramites','tramites.add_tramites','tramites.delete_tramites','tramites.change_tramites')
    success_url = reverse_lazy ('tramites:listar_tramites')

class CrearModalTramites(ValidarPermisosRequeridosMixin,CreateView):
    model = Tramites
    template_name = 'tramites/modalcreartramites.html'
    permission_required = ('tramites.view_tramites','tramites.add_tramites','tramites.delete_tramites','tramites.change_tramites')
    form_class = TramitesForm
    success_url = reverse_lazy ('tramites:listar_tramites')

class EliminarTramites(ValidarPermisosRequeridosMixin,DeleteView):
    model = Tramites
    permission_required = ('tramites.view_tramites','tramites.add_tramites','tramites.delete_tramites','tramites.change_tramites')
    success_url = reverse_lazy ('tramites:listar_tramites')


#Clases para Casillero#

class ListarCasilleros(ValidarPermisosRequeridosMixin,ListView):
    model = Casilleros3
    template_name = 'tramites/listar_casilleros.html'
    permission_required = ('tramites.view_casilleros3','tramites.add_casilleros3','tramites.delete_casilleros3','tramites.change_casilleros3')
    context_object_name = 'casilleros'
    queryset = Casilleros3.objects.all()


class EditarCasilleros(ValidarPermisosRequeridosMixin,UpdateView):
    model = Casilleros3
    template_name = 'tramites/modalcasilleros.html'
    permission_required = ('tramites.view_casilleros3','tramites.add_casilleros3','tramites.delete_casilleros3','tramites.change_casilleros3')
    form_class = CasillerosForm
    success_url = reverse_lazy ('tramites:listar_casilleros')


class CrearCasilleros(ValidarPermisosRequeridosMixin,CreateView):
    model = Casilleros3
    form_class = CasillerosForm
    template_name = 'tramites/crear_casilleros.html'
    permission_required = ('tramites.view_casilleros3','tramites.add_casilleros3','tramites.delete_casilleros3','tramites.change_casilleros3')
    success_url = reverse_lazy ('tramites:listar_casilleros')

class CrearModalCasilleros(ValidarPermisosRequeridosMixin,CreateView):
    model = Casilleros3
    template_name = 'tramites/modalcrearcasilleros.html'
    permission_required = ('tramites.view_casilleros3','tramites.add_casilleros3','tramites.delete_casilleros3','tramites.change_casilleros3')
    form_class = CasillerosForm
    success_url = reverse_lazy ('tramites:listar_casilleros')

class EliminarCasilleros(ValidarPermisosRequeridosMixin,DeleteView):
    model = Casilleros3
    permission_required = ('tramites.view_casilleros3','tramites.add_casilleros3','tramites.delete_casilleros3','tramites.change_casilleros3')
    success_url = reverse_lazy ('tramites:listar_casilleros')

@permission_required('tramites.view_casilleros3',login_url='home')
@permission_required('tramites.add_casilleros3',login_url='home')
@permission_required('tramites.delete_casilleros3',login_url='home')
@permission_required('tramites.change_casilleros3',login_url='home')
def buscar_casilleros(request):
        busqueda = request.GET.get("buscar")
        casilleros = Casilleros3.objects.all().order_by('-casillero')
        paginator = Paginator(casilleros, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        

        if busqueda:
            casilleros = Casilleros3.objects.filter(
                Q (usuario__nombre__icontains = busqueda) |
                Q (usuario__id__icontains = busqueda) |
                Q (casillero__icontains= busqueda) |
                Q (co_titulares__icontains= busqueda) |
                 Q (autorizados_a_retirar__icontains= busqueda)
            ).distinct()
            return render(request, 'tramites/listar_casilleros.html', {'casilleros':casilleros})
        else:
            return render(request, 'tramites/listar_casilleros.html', {'casilleros': page_obj})




#Clases para ClientesTramites#

class ListarClientes_Tramites(ValidarPermisosRequeridosMixin,ListView):
    model = Clientes_Tramites
    template_name = 'tramites/listar_clientes_tramites.html'
    permission_required = ('tramites.view_clientes_tramites','tramites.add_clientes_tramites','tramites.delete_clientes_tramites','tramites.change_clientes_tramites')
    context_object_name = 'clientes_tramites'
    queryset = Clientes_Tramites.objects.all()
    paginate_by = 1



    

class EditarClientes_Tramites(ValidarPermisosRequeridosMixin,UpdateView):
    model = Clientes_Tramites
    template_name = 'tramites/modalClientes_tramites.html'
    permission_required = ('tramites.view_clientes_tramites','tramites.add_clientes_tramites','tramites.delete_clientes_tramites','tramites.change_clientes_tramites')
    form_class = Clientes_TramitesForm
    success_url = reverse_lazy ('tramites:listar_clientes_tramites')


class CrearClientes_Tramites(ValidarPermisosRequeridosMixin,CreateView):
    model = Clientes_Tramites
    form_class = Clientes_TramitesForm
    template_name = 'tramites/crear_clientes_tramites.html'
    permission_required = ('tramites.view_clientes_tramites','tramites.add_clientes_tramites','tramites.delete_clientes_tramites','tramites.change_clientes_tramites')
    success_url = reverse_lazy ('tramites:listar_clientes_tramites')

class CrearModalClientes_Tramites(ValidarPermisosRequeridosMixin,CreateView):
    model = Clientes_Tramites
    template_name = 'tramites/modalcrearclientes_tramites.html'
    permission_required = ('tramites.view_clientes_tramites','tramites.add_clientes_tramites','tramites.delete_clientes_tramites','tramites.change_clientes_tramites')
    form_class = Clientes_TramitesForm
    success_url = reverse_lazy ('tramites:listar_clientes_tramites')
    

class EliminarClientes_Tramites(ValidarPermisosRequeridosMixin,DeleteView):
    model = Clientes_Tramites
    permission_required = ('tramites.view_clientes_tramites','tramites.add_clientes_tramites','tramites.delete_clientes_tramites','tramites.change_clientes_tramites')
    success_url = reverse_lazy ('tramites:listar_clientes_tramites')

@permission_required('tramites.view_clientes_tramites',login_url='home')
@permission_required('tramites.add_clientes_tramites',login_url='home')
@permission_required('tramites.delete_clientes_tramites',login_url='home')
@permission_required('tramites.change_clientes_tramites',login_url='home')
def buscar_clientes_tramites(request):
        busqueda = request.GET.get("buscar")
        clientes_tramites = Clientes_Tramites.objects.all().order_by('-id')
        paginator = Paginator(clientes_tramites, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        """
        def listing(request):
                contact_list = Clientes_Tramites.objects.all()
                paginator = Paginator(contact_list, 2) # Show 25 contacts per page.
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, 'tramites/listar_clientes_tramites.html', {'clientes_tramites': page_obj})
                """
        if busqueda:
                clientes_tramites = Clientes_Tramites.objects.filter(
                    Q (autos__icontains = busqueda) |
                    Q (usuario__nombre__icontains= busqueda) |
                    Q (tramite_id__nombre_tramite__icontains= busqueda) |
                    Q (id__icontains = busqueda) |
                    Q (usuario__id__icontains= busqueda)
                ).distinct()
                return render(request, 'tramites/listar_clientes_tramites.html', {'clientes_tramites':clientes_tramites})
        else:
            return render(request, 'tramites/listar_clientes_tramites.html', {'clientes_tramites': page_obj})

@permission_required('tramites.view_clientes_tramites',login_url='home')
@permission_required('tramites.add_clientes_tramites',login_url='home')
@permission_required('tramites.delete_clientes_tramites',login_url='home')
@permission_required('tramites.change_clientes_tramites',login_url='home')
def buscar_clientes_tramites_fechas(request):
        fecha_clientes_tramites = Clientes_Tramites.objects.all().order_by('-id')
        paginator = Paginator(fecha_clientes_tramites, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if request.method == 'POST':
            try:
            
                fecha_clientes_tramites_desde = request.POST ['fecha_clientes_tramites_desde']
                fecha_clientes_tramites_hasta = request.POST ['fecha_clientes_tramites_hasta']

                fecha_clientes_tramites = Clientes_Tramites.objects.filter(fecha_creacion__range=(fecha_clientes_tramites_desde, fecha_clientes_tramites_hasta))        
                return render(request, 'tramites/listar_clientes_tramites_busqueda.html', {'fecha_clientes_tramites':fecha_clientes_tramites})     

            except:
                return render(request,'tramites/listar_clientes_tramites_busqueda.html', {'fecha_clientes_tramites':page_obj})
        else:
            return render(request,'tramites/listar_clientes_tramites_busqueda.html', {'fecha_clientes_tramites':page_obj})

def buscar_usuarios_tramites(request):
        busqueda = request.GET.get("buscar")
        clientes_tramites_usuarios = Clientes_Tramites.objects.filter(usuario = request.user)
        paginator = Paginator(clientes_tramites_usuarios, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if busqueda:
                clientes_tramites_usuarios = Clientes_Tramites.objects.filter(usuario = request.user)

                return render(request, 'tramites/listar_usuarios_tramites.html', {'clientes_tramites_usuarios':clientes_tramites_usuarios})
        else:
            return render(request, 'tramites/listar_usuarios_tramites.html', {'clientes_tramites_usuarios': page_obj})


"""
class ListadoPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('tramites/listar_clientes_tramites.html')
        context = {'title' : 'Imprimir listado'}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
"""

#Clases para Cédulas#

class ListarCedulas(ValidarPermisosRequeridosMixin,ListView):
    model = Cedulas1
    template_name = 'tramites/listar_cedulas.html'
    permission_required = ('tramites.view_cedulas1','tramites.add_cedulas1','tramites.delete_cedulas1','tramites.change_cedulas1')
    context_object_name = 'cedulas'
    queryset = Cedulas1.objects.all()
    

class EditarCedulas(ValidarPermisosRequeridosMixin,UpdateView):
    model = Cedulas1
    template_name = 'tramites/modalCedulas.html'
    permission_required = ('tramites.view_cedulas1','tramites.add_cedulas1','tramites.delete_cedulas1','tramites.change_cedulas1')
    form_class = CedulasForm
    success_url = reverse_lazy ('tramites:listar_cedulas')


class CrearCedulas(ValidarPermisosRequeridosMixin,CreateView):
    model = Cedulas1
    form_class =  CedulasForm
    template_name = 'tramites/crear_cedulas.html'
    permission_required = ('tramites.view_cedulas1','tramites.add_cedulas1','tramites.delete_cedulas1','tramites.change_cedulas1')
    success_url = reverse_lazy ('tramites:listar_cedulas')

class CrearModalCedulas(ValidarPermisosRequeridosMixin,CreateView):
    model = Cedulas1
    template_name = 'tramites/modalcrearcedulas.html'
    permission_required = ('tramites.view_cedulas1','tramites.add_cedulas1','tramites.delete_cedulas1','tramites.change_cedulas1')
    form_class =  CedulasForm
    success_url = reverse_lazy ('tramites:listar_cedulas')

class EliminarCedulas(ValidarPermisosRequeridosMixin,DeleteView):
    model = Cedulas1
    permission_required = ('tramites.view_cedulas1','tramites.add_cedulas1','tramites.delete_cedulas1','tramites.change_cedulas1')
    success_url = reverse_lazy ('tramites:listar_cedulas')

@permission_required('tramites.view_cedulas1',login_url='home')
@permission_required('tramites.add_cedulas1',login_url='home')
@permission_required('tramites.delete_cedulas1',login_url='home')
@permission_required('tramites.change_cedulas1',login_url='home')
def buscar_cedulas(request):
        busqueda = request.GET.get("buscar")
        cedulas = Cedulas1.objects.all().order_by('-id')
        paginator = Paginator(cedulas, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        def listing(request):
            contact_list = Cedulas1.objects.all()
            paginator = Paginator(contact_list, 2) # Show 25 contacts per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'tramites/listar_cedulas.html', {'cedulas': page_obj})

        if busqueda:
            cedulas = Cedulas1.objects.filter(
                Q (autos__icontains = busqueda) |
                Q (id__icontains = busqueda) |
                Q (casillero_id__casillero__icontains= busqueda) | 
                Q (casillero_id__co_titulares__icontains = busqueda) |
                Q (casillero_id__autorizados_a_retirar__icontains= busqueda)
            ).distinct()
            return render(request, 'tramites/listar_cedulas.html', {'cedulas':cedulas})
        else:
            return render(request, 'tramites/listar_cedulas.html', {'cedulas': page_obj})

@permission_required('tramites.view_cedulas1',login_url='home')
@permission_required('tramites.add_cedulas1',login_url='home')
@permission_required('tramites.delete_cedulas1',login_url='home')
@permission_required('tramites.change_cedulas1',login_url='home')
def buscar_cedulas_fechas(request):
        fecha_cedulas = Cedulas1.objects.all().order_by('-id')
        paginator = Paginator(fecha_cedulas, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if request.method == 'POST':
            try:
                
                    fecha_desde = request.POST ['fecha_desde']
                    fecha_hasta = request.POST ['fecha_hasta']

                    fecha_cedulas = Cedulas1.objects.filter(fecha_creacion__range=(fecha_desde, fecha_hasta))     
                    return render(request, 'tramites/listar_cedulas_busqueda.html', {'fecha_cedulas':fecha_cedulas})  
            except:
             return render(request,'tramites/listar_cedulas_busqueda.html', {'fecha_cedulas':page_obj})
        else:
            return render(request,'tramites/listar_cedulas_busqueda.html', {'fecha_cedulas':page_obj})


def buscar_usuarios_cedulas(request):
        busqueda = request.GET.get("buscar")
        cedulas_usuarios = Cedulas1.objects.filter(usuario = request.user)
        paginator = Paginator(cedulas_usuarios, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if busqueda:
                cedulas_usuarios = Cedulas1.objects.filter(usuario = request.user)

                return render(request, 'tramites/listar_usuarios_cedulas.html', {'cedulas_usuarios':cedulas_usuarios})
        else:
            return render(request, 'tramites/listar_usuarios_cedulas.html', {'cedulas_usuarios': page_obj})

"""
class Usuarios_tramites(ListView):
    model: Clientes_Tramites_Usuarios
    paginate_by: 6
    form_class = Clientes_Tramites_usuarioForm
    template_name = 'tramites/listar_usuarios_tramites.html'
    
    def get_queryset(self):
        queryset = self.model.objects.filter(usuario = request.user)
        return queryset
     

class CrearUsuarios_tramites(CreateView):
    model = Clientes_Tramites_Usuarios
    form_class =  Clientes_Tramites_usuarioForm
    template_name = 'tramites/modalcrearusuarios_tramites.html'
    success_url = reverse_lazy ('tramites:listar_usuarios_tramites')
"""

#Clases para Firmas#
"""
class ListarFirmas(ListView):
    model = JSignatureModel
    template_name = 'tramites/listar_firmas.html'
    context_object_name = 'firmas'
    queryset = JSignatureModel.objects.all()


    


def my_view(request):
    form = SignatureForm(request.POST)
    if form.is_valid():
        signature = form.cleaned_data.get('signature')
        if signature:
            signature_picture = draw_signature(signature)
        return render(request, 'tramites/listar_firmas.html', {'form': form })


    

class EditarFirmas(UpdateView):
    model = JSignatureModel
    template_name = 'tramites/modalFirmas.html'
    form_class = SignatureForm
    success_url = reverse_lazy ('tramites:listar_firmas')


def buscar_firmas(request):
        busqueda = request.GET.get("buscar")
        firmas = JSignatureModel.objects.all()

class CrearFirmas(CreateView):
    model = JSignatureModel
    form_class = SignatureForm
    template_name = 'tramites/modalcrearfirmas.html'
    success_url = reverse_lazy ('tramites:listar_firmas')



class CrearModalFirmas(CreateView):
    model = JSignatureModel
    template_name = 'tramites/modalcrearfirmas.html'
    form_class = SignatureForm
    success_url = reverse_lazy ('tramites:listar_firmas')
    

class EliminarFirmas(DeleteView):
    model = JSignatureModel
    success_url = reverse_lazy ('tramites:listar_firmas')

"""




