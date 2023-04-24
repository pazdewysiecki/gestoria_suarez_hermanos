from email.policy import default
from inspect import signature
from tabnanny import verbose
from django.db import models
from django import forms
from jsignature.fields import JSignatureField
from jsignature.widgets import JSignatureWidget
from jsignature.mixins import JSignatureFieldsMixin
from usuario2.models import Usuario

#from ckeditor import RichTextField


class Tramites (models.Model):
    id = models.AutoField(primary_key= True)
    nombre_tramite = models.CharField(max_length = 200, blank = False, verbose_name='nombre_tramite')
    descripcion_tramite = models.TextField(blank = True, verbose_name='descripcion_tramite')

    def __str__(self):
        return str(self.nombre_tramite)
         

    class Meta:
        ordering = ['nombre_tramite']
        verbose_name = 'Tramite'
        verbose_name_plural = 'Tramites'
"""
class Clientes (models.Model):
    id = models.AutoField(primary_key= True)
    nombre_cliente = models.CharField(max_length = 200, blank = False, verbose_name='nombre_cliente')
    telefono_cliente = models.CharField(max_length = 100, blank = False, verbose_name='telefono_cliente')
    mail_cliente = models.EmailField(max_length = 200, blank = False, verbose_name='mail_cliente')


    def __str__(self):
        return str(self.nombre_cliente)

    class Meta:
        ordering = ['nombre_cliente']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
"""

class Casilleros3 (models.Model):
    casillero = models.IntegerField(primary_key= True, blank = True, verbose_name='casillero')
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE, null=True)
    vigencia_desde = models.DateField(max_length = 99, blank = True, verbose_name='vigencia_desde')
    vigencia_hasta = models.DateField(max_length = 100, blank = True, verbose_name='vigencia_hasta')
    co_titulares = models.CharField(max_length = 200, blank = True, verbose_name='co_titulares')
    autorizados_a_retirar = models.CharField(max_length = 200, blank = True, verbose_name='autorizados_a_retirar')
    precio = models.IntegerField(blank = False, verbose_name='precio', null=True)
    #existe un campo URLField para links 
    #abogado_cliente = models.ForeignKey(Abogados, on_delete = models.CASCADE, null=True)


    """
    def save(self, *args, **kwargs):
       if not Clientes.objects.count():
          self.id = 40000
       else:
          self.id = Clientes.objects.last().id + 1
       super(Clientes, self).save(*args, **kwargs)
     """


    def __str__(self):
        return str(self.casillero)

    class Meta:
        ordering = ['casillero']
        verbose_name = 'Casillero'
        verbose_name_plural = 'Casilleros'



class Clientes_Tramites (models.Model):
    id = models.AutoField(primary_key= True)
    fecha_creacion = models.DateField('Fecha Creacion',auto_now=False , auto_now_add=True)
   # cliente_id = models.OneToOneField(Clientes, on_delete = models.CASCADE)
   # tramite_id = models.OneToOneField(Tramites, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE, null=True)
    tramite_id = models.ForeignKey(Tramites, on_delete = models.CASCADE, null=True)
    autos = models.CharField(max_length = 200, blank = False, verbose_name='autos', null=True)
    estado_tramite_iniciado = models.BooleanField ('Iniciado', default=True)
    estado_tramite_finalizado = models.BooleanField ('Finalizado', default=False)
    estado_tramite_anulado = models.BooleanField ('Anulado', default=False)
    comentarios_tramite = models.TextField(blank = True, verbose_name='comentarios_tramite')
    precio_tramite = models.IntegerField(blank = False, verbose_name='precio_tramite', null=True)
    firma = models.CharField(max_length = 200,blank = True, verbose_name='firma')
    
   # cliente_id = models.ManyToManyField(Clientes)
   # tramite_id = models.ManyToManyField(Tramites)

    def __str__(self):
        return str(self.id)
    """
    def save(self, *args, **kwargs):
       if not Clientes_Tramites.objects.count():
          self.id = 30000
       else:
          self.id = Clientes_Tramites.objects.last().id + 1
       super(Clientes_Tramites, self).save(*args, **kwargs)
     """
    class Meta:
        ordering = ['id']
        verbose_name = 'Clientes_Tramites'
        verbose_name_plural = 'Clientes_Tramite'
"""
class Clientes_Tramites_Usuarios (models.Model):
    id = models.AutoField(primary_key= True)
    cliente_id = models.ForeignKey(Clientes_Tramites, on_delete = models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'cliente_tramite_usuario'
        verbose_name_plural = 'cliente_tramite_usuario'
"""

class Cedulas1 (models.Model):
    id = models.AutoField(primary_key= True)
    fecha_creacion = models.DateField('Fecha Creacion',auto_now=False , auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE, null=True)
    casillero_id = models.ForeignKey(Casilleros3, on_delete = models.CASCADE, null=True)
    autos = models.CharField(max_length = 200, blank = False, verbose_name='autos', null=True)
    comentarios_cedula = models.TextField(blank = True, verbose_name='comentarios_cedula')
    firma = models.CharField(max_length = 200,blank = True, verbose_name='firma')


    def __str__(self):
        return str(self.id)
    """
    def save(self, *args, **kwargs):
       if not Cedulas1.objects.count():
          self.id = 50000
       else:
          self.id = Cedulas1.objects.last().id + 1
       super(Cedulas1, self).save(*args, **kwargs)
   """
    class Meta:
        ordering = ['id']
        verbose_name = 'Cedula'
        verbose_name_plural = 'Cedulas'

"""
class JSignatureModel (JSignatureFieldsMixin):
    id = models.AutoField(primary_key= True)
    fecha_creacion = models.DateField('Fecha Creacion',auto_now=False , auto_now_add=True)
    cliente_tramite_id = models.ForeignKey(Clientes_Tramites, on_delete = models.CASCADE, null=True)
    signature = models.CharField(max_length = 200, blank = True, verbose_name='firma', null=True)

    def __str__(self):
        return str(self.id)
   
    class Meta:
        ordering = ['id']
        verbose_name = 'Signature'
        verbose_name_plural = 'Signatures'
"""
"""
home:

                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Firmas</a>
                            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="{% url 'tramites:crear_firmas'%}">Crear Firmas</a></li>
                                <li><a class="dropdown-item" href="{% url 'tramites:listar_firmas'%}">Buscar Firmas</a></li>
                            </ul>
                        </li>

"""