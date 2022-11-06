from django.urls import path

from app.views import (atualizar, criar, deletar, editar, formulario, home,
                       visualizar)

urlpatterns = [
    path('', home, name='home'),
    path('formulario/', formulario, name='formulario'),
    path('criar/', criar, name='criar'),
    path('visualizar/<int:pk>/', visualizar, name='visualizar'),
    path('editar/<int:pk>/', editar, name='editar'),
    path('atualizar/<int:pk>/', atualizar, name='atualizar'),
    path('deletar/<int:pk>/', deletar, name='deletar'),



]

