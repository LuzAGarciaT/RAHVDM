from django.shortcuts import get_object_or_404, redirect, render

from teacher.forms import TeacherForm
from teacher.models import Teacher

# Create your views here.

def create_teachers(request):
    if request.method == "GET":
        return render(request, "create_teacher.html", {"form": TeacherForm()})
    else:
        form = TeacherForm(request.POST)
        print(form.is_valid())

        print(form.errors)
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.save()
            return redirect("teacher")
            
        else:
            return render(
                request,
                "create_teacher.html",
                {"form": form, "error": "Error creando el empleado"},
                )
        
def teacher(request):
    teachers = Teacher.objects.all()  # Obtén todos los empleados de la base de datos
    return render(request, 'teacher.html', {'teachers': teachers})

def teachers_edit(request, teachers_idteacher):
    teacher = get_object_or_404(Teacher, idteacher=teachers_idteacher)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            print(request, 'El teacher se ha actualizado correctamente.')
            return redirect("teacher")
        else:
            print(request, 'Hubo un error al actualizar el teacher.')
            print(form.errors)
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "edit_teacher.html", {"teacher": teacher, "form": form})
