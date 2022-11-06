from django.core.paginator import Paginator
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from app.forms import CarrosForm
from app.models import Carros

# Create your views here.

def home(request):
    data={}
    todos_os_dados = Carros.objects.all() #recebe todos os registros do banco dados
    paginator = Paginator(todos_os_dados, 10) #recebe todos registros, exibe apenas 2
    paginas = request.GET.get('pagina') 
    data['banco_de_dados'] = paginator.get_page(paginas)
    return render(request, 'home.html', data)


def formulario(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'formulario.html', data)


def criar(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def visualizar(request, pk):
    data = {}
    data['banco_de_dados'] = Carros.objects.get(pk=pk)
    return render(request, 'visualizar.html', data)


def editar(request, pk): 
    data = {}
    data['banco_de_dados'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['banco_de_dados'])
    return render(request, 'formulario.html', data)


def atualizar(request, pk):
    data = {}
    data['banco_de_dados'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['banco_de_dados'])
    if form.is_valid():
        form.save()
        return redirect('home')
    

def deletar(request, pk):
    banco_de_dados = Carros.objects.get(pk=pk)
    banco_de_dados.delete()
    return redirect('home')

    
