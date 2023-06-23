from django.shortcuts import get_object_or_404, redirect, render
from rol.forms import RolForm
from rol.models import Rol


def inicio(request):
    return render(request, 'inicio.html')


def create_roles(request):
    if request.method == "GET":
        return render(request, "create_rol.html", {"form": RolForm()})
    else:
        form = RolForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.save()
            return redirect("rol")
            
        else:
            return render(
                request,
                "create_rol.html",
                {"form": form, "error": "Error creando el empleado"},
                )
        
def rol(request):
    roles = Rol.objects.all()  # Obtén todos los empleados de la base de datos
    return render(request, 'rol.html', {'roles': roles})

def roles_edit(request, roles_idrol):
    rol = get_object_or_404(Rol, idrol=roles_idrol)
    if request.method == "POST":
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            print(request, 'El rol se ha actualizado correctamente.')
            return redirect("rol")
        else:
            print(request, 'Hubo un error al actualizar el rol.')
            print(form.errors)
    else:
        form = RolForm(instance=rol)
    return render(request, "roles_edit.html", {"rol": rol, "form": form})
