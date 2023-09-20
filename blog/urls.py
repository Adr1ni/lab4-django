from django.urls import path
from . import views

urlpatterns = [
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('entradas_autor/<int:id>/',views.autoures_entradas, name='autor_entradas'),
]
