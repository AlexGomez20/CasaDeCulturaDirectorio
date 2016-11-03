from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from herramientas import *
from models import *
from forms import *

# Create your views here.

def home(request):
    logeado = False
    u = None
    admin = False

    if request.user.is_authenticated:
        logeado = True
        u = request.user.perfil.nombreArtista
        if request.user.perfil.rol.is_admin():
            admin = True

    capsula = Capsulas.public.all()
    if len(capsula) is not 0:
         capsula =capsula[0]
    context = {
        'capsula' : capsula,
        'logeado' : logeado,
        'usuario' : u,
        'admin' : admin,
        'user' : request.user
    }
    return render(request, 'inicio.html', context)

def perfil_list(request):
    perfil = Perfil.public.all()
    context = {'perfil': perfil}
    return render(request, 'perfil_list.html', context)

def actividad_list(request):
    actividad = Actividad.public.all()
    context = {'actividad': actividad}
    return render(request, 'actividad_list.html', context)

@login_required
def actividad_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        actividad = Actividad.public.all()
    else:
        actividad = Actividad.public.filter(user_username=username)
    context = {'actividad': actividad, 'perfil': user}
    return render(request, 'actividad_user.html', context)

class EventosDetailView(DetailView):
    model = Perfil

    def get_context_data(self, **kwargs):
        context = super(EventosDetailView, self).get_context_data(**kwargs)
        actividades = Actividad.objects.filter(perfil=context['object']).order_by('fechaRealizacion')
        context = {'actividad': actividades}
        return context

def perfil_create(request):
    if request.method == 'POST':
        form = PerfilForm(data=request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.save()
            form.save_m2m()
    else:
        form = PerfilForm()
    context = {'form': form, 'create': True}
    return render(request, 'form.html', context)

@login_required
def perfil(request, username):
    user = get_object_or_404(User, username=username)
    is_owner = False
    if request.user == user:
        perfil = user.perfil
        is_owner = True
    else:
        perfil = Perfil.public.filter(user_username=username)

    context = {
        'perfil': perfil,
        'es_propietario': is_owner,
    }
    return render(request, 'mi_perfil.html', context)

@login_required
def perfil_edit(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        form = PerfilForm(instance=perfil, data=request.POST)
        if form.is_valid():
            print "si"
            #form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('home:home'))
    else:
        print "no"
        form = PerfilForm(instance=perfil)
    context = {'form': form, 'create': False}
    return render(request, 'form.html', context)

@login_required
def actividad_create(request,username=''):
    if request.method == 'POST':
        form = ActividadForm(data=request.POST)
        if form.is_valid():
            print "formulario actividad valido"
            actividad = form.save(commit=False)
            actividad.fechaPublicacion = date.today()

            img = request.FILES['imagen']
            img.name = renombrar_archivo(img.name,newName='actividad')
            actividad.imagen = img

            actividad.save()
            actividad.perfil.add(request.user.perfil)

            form.save_m2m()

            reescalar_imagen(actividad.imagen.path,actividad.imagen.path)

            return HttpResponseRedirect(reverse('home:home'))
    else:
        form = ActividadForm()

    context = {'form': form, 'create': True}
    return render(request, 'crearActividad.html', context)

@login_required
def capsula_create(request):
    if request.user.perfil.rol.is_admin() != True:
        return HttpResponseRedirect(reverse('error'))

    if request.method == 'POST':
        form = CapsulaForm(data=request.POST)
        if form.is_valid():
            capsula = form.save(commit=False)
            capsula.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('home:perfil',kwargs={'username': request.user.username,}))
    else:
        form = CapsulaForm()

    context = {'form': form, 'create': True}
    return render(request, 'capsulas.html', context)

@login_required
def administracion(request):

    if request.user.perfil.rol.is_admin() != True:
        return HttpResponseRedirect(reverse('error'))

    u = request.user.perfil.nombreArtista
    context = {
        'usuario' : u,
        }
    return render(request, 'Admi.html', context)

@login_required
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('home:home'))

def ingresar(request):
    next = ""
    error = False

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home:perfil',kwargs={'username': request.user.username,}))

    if request.GET:
        next = request.GET['next']

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next == "":
                    return HttpResponseRedirect(reverse('home:home'))
                else:
                    return HttpResponseRedirect(next)
            else:
                #el usuario no esta activo
                pass
        else:
            error = True
            form = LoginForm()
        #    return HttpResponseRedirect('/login/')
    else:
        form = LoginForm()

    context = {'form': form, 'create': True, 'next':next, 'error':error,}
    return render(request, 'login.html', context)

def error(request):
    return render(request, 'error.html')

def actividad_detail(request, username='', id='0'):
    logeado = False
    u = None
    admin = False
    actividad = Actividad.objects.filter(id=id)
    print actividad[0].nombre

    if request.user.is_authenticated:
        logeado = True
        u = request.user.username
        if request.user.perfil.rol.is_admin():
            admin = True

    context = {
        'logeado' : logeado,
        'usuario' : u,
        'admin' : admin,
    }
    return render(request, 'detalle_actividad.html', context)
