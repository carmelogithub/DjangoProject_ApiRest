# core/views.py

from django.shortcuts import render
from .forms import AccionForm
from .services import procesar_datos
import requests

def formulario_view(request):
    resultado = None

    if request.method == 'POST':
        form = AccionForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            accion = form.cleaned_data['accion']

            # Llamada a función privada (no visible al usuario)
            resultado = procesar_datos(nombre, email, accion)

            # Enviar a API externa (opcional)
            try:
                response = requests.post(
                    'http://localhost:3001/contactos',
                    json={
                        'nombre': nombre,
                        'email': email,
                        'accion': accion
                    },
                    timeout=5
                )
                if response.status_code == 201:
                    resultado += " (Datos enviados correctamente a API)"
                else:
                    resultado += f" (Error en API: {response.status_code})"
            except Exception as e:
                resultado += f" (Error enviando a API externa: {e})"

    else:
        form = AccionForm()

    return render(request, 'app/form.html',
                  {'form': form, 'resultado': resultado})

def vista_lista(request):
    datos=[]
    try:
        response=requests.get('http://localhost:3001/contactos',timeout=5)
        if response.status_code == 200:
            datos=response.json()
    except Exception as e:
        print(f"Error al conectar {e}")
    return render(request, 'app/lista.html',{'datos': datos})