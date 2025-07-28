from django.urls import path
from .views import formulario_view, vista_lista

urlpatterns = [
    path('', formulario_view, name='formulario'),
path('lista/', vista_lista, name='lista'),
]
