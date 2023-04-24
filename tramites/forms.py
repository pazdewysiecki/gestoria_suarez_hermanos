from dataclasses import field, fields
import imp
from django import forms


from .models import Casilleros3, Tramites, Clientes_Tramites, Cedulas1

class TramitesForm(forms.ModelForm):
    class Meta:
        model = Tramites
        fields = ['nombre_tramite', 'descripcion_tramite','id']
        labels = {
                'nombre_tramite': "Nombre del trámite:",
                'descripcion_tramite': "Descripción del trámite:",
                'id': "Código Genérico del trámite:",
            }
        widgets = {
            'nombre_tramite': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el trámite',
                    'id':'nombre_tramite'
                }
            ),
            'descripcion_tramite': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese un comentario sobre el trámite',
                    'id':'descripcion_tramite'
                }
            )
        }

"""
class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre_cliente', 'telefono_cliente', 'mail_cliente', 'id']     
        labels = {
                'nombre_cliente': "Nombre completo:",
                'telefono_cliente': "Teléfono:",
                'mail_cliente': "Mail:",
                'id': "Código del cliente:",
            }
        widgets = {
            'nombre_cliente': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre completo del cliente',
                    'id':'nombre_cliente'
                }
            ),
            'telefono_cliente': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el teléfono del cliente',
                    'id':'telefono_cliente'
                }
            ),
             'mail_cliente': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el mail del cliente',
                    'id':'mail_cliente'
                }
            ),           
        }
"""

class CasillerosForm(forms.ModelForm):
    class Meta:
        model = Casilleros3
        fields = ['usuario', 'casillero', 'vigencia_desde','vigencia_hasta','co_titulares','autorizados_a_retirar', 'precio']     
        labels = {
                'usuario': "Código del cliente:",
                'casillero': "Casillero",
                'vigencia_desde': "Vigencia desde:",
                'vigencia_hasta': "Vigencia hasta:",
                'id': "Código del cliente:",
                'co_titulares': "Có-titulares:",
                'autorizados_a_retirar': "Autorizados a retirar:",
                'precio': "Precio:",
            }
        widgets = {
            'usuario': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el código del cliente',
                    'id':'usuario'
                }
            ),
            'casillero': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el casillero del cliente',
                    'id':'casillero'
                }
            ),
             'vigencia_desde': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Fecha de inicio de vigencia del casillero ingrese (/mm/dd/aaaa):',
                    'id':'vigencia_desde'
                }
            ),
            'vigencia_hasta': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Fecha de vencimiento del casillero ingrese (/mm/dd/aaaa):',
                    'id':'vigencia_hasta'
                }
            ),   
             'co_titulares': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los cotitulares del casillero',
                    'id':'co_titulares'
                }
            ), 
            'autorizados_a_retirar': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los Autorizados a retirar:',
                    'id':'autorizados_a_retirar'
                }
            ),  
           'precio': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el valor del casillero:',
                    'id':'precio'
                }
            ),             
        }

class Clientes_TramitesForm(forms.ModelForm):
    class Meta:
        model = Clientes_Tramites
        fields = ['usuario', 'tramite_id', 'autos','estado_tramite_iniciado','estado_tramite_finalizado','estado_tramite_anulado','comentarios_tramite','precio_tramite','firma','id']
        labels = {
                'usuario': "Código del cliente:",
                'tramite_id': "Nuevo trámite:",
                'autos': "Autos:",
                'id': "Código del nuevo trámite:",
                'estado_tramite_iniciado': "Trámite iniciado:",              
                'estado_tramite_finalizado': "Trámite finalizado:",
                'estado_tramite_anulado': "Trámite anulado:",
                'comentarios_tramite': "Comentarios adicionales del trámite:",
                'precio_tramite': "Precio:",
                'firma': "Firma",
            }
        widgets = {
            'usuario': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el código del cliente',
                    'id':'usuario'
                }
            ),
            'tramite_id': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el código del nuevo trámite',
                    'id':'tramite_id'
                }
            ),
             'autos': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese autos',
                    'id':'autos'
                }
            ),
             'comentarios_tramite': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese comentarios adicionales al trámite',
                    'id':'comentarios_tramite'
                 }
             ),
            'precio_tramite': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el valor del trámite:',
                    'id':'precio_tramite'
                }
            )   
        }

class CedulasForm(forms.ModelForm):
    class Meta:
        model = Cedulas1
        fields = ['casillero_id','usuario', 'autos','comentarios_cedula','firma','id']
        labels = {
                'casillero_id': "Código de casillero:",
                'autos': "Autos:",
                'id': "Código de la nueva cédula:",
                'usuario': "Código del cliente:",
                'comentarios_cedula': "Comentarios adicionales de la cédula:",
                'firma': "Firma",
            }
        widgets = {
            'casillero_id': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el código del casillero:',
                    'id':'casillero_id'
                }
            ),
            'usuario': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el código del cliente',
                    'id':'usuario'
                }
            ),
             'autos': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese autos',
                    'id':'autos'
                }
            ),
             'comentarios_cedula': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese comentarios adicionales a la cédula',
                    'id':'comentarios_cedula'
                 }
             )
        }
"""
class FirmasForm(forms.ModelForm):
    class Meta:
        model = Firmas
        fields = ['cliente_tramite_id','firma','id']
        firma = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#e0b642', 'height': '200px'}))


class SignatureForm(forms.Form):
    signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

"""
"""
class Clientes_Tramites_usuarioForm(forms.ModelForm):
    class Meta:
        model = Clientes_Tramites_Usuarios
        fields = ['cliente_id', 'id', 'usuario']
        labels = {
                'cliente_id': "Código del cliente:",
                'id': "Código del nuevo trámite usuario:",
                'usuario': "usuario:",            
            }
        widgets = {
            'cliente_id': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el código del cliente',
                    'id':'cliente_id'
                }
            ),
            'usuario': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese usuario',
                    'id':'usuario'
                }
            ),     
        }
"""