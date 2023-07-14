from django.shortcuts import render, redirect

from logros.models import Logro
from .forms import LogroForm

def uploadlogro(request):
    if request.method == 'POST':
        form = LogroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('logros')  # Reemplaza 'nombre_de_la_vista' con el nombre de la vista a la que deseas redirigir después de guardar el logro
    else:
        form = LogroForm()
    
    return render(request, 'uploadlogro.html', {'form': form})


def logros(request):
    logros = Logro.objects.all()
    return render(request, 'logros.html', {'logros': logros})