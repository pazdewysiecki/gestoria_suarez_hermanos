"""suarezhermanos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,logout_then_login
from django.contrib.auth.decorators import login_required
from tramites.views import Inicio, InicioSistema
from django.conf import settings
from django.conf.urls.static import static
from usuario2.views import Login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include(('usuario2.urls', 'usuarios'))),
    path('tramites/',include(('tramites.urls','tramites'))),
    path('',Inicio.as_view(), name = 'index'),
    path('home',login_required(InicioSistema.as_view()), name = 'home'),
    path('accounts/login/', Login.as_view(),{'template_name':'login.html'}, name = 'login'),
    path ('logout/', logout_then_login, name = 'logout')
    ]