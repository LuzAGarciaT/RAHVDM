from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render

from student.forms import StudentForm
from student.models import Student

# Create your views here.

def create_students(request):
    if request.method == "GET":
        return render(request, "create_student.html", {"form": StudentForm()})
    else:
        form = StudentForm(request.POST)
        print(form.is_valid())

        print(form.errors)
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.save()
            return redirect("student")
            
        else:
            return render(
                request,
                "create_student.html",
                {"form": form, "error": "Error creando el empleado"},
                )
        
def student(request):
    students = Student.objects.all()  # Obtén todos los empleados de la base de datos
    return render(request, 'student.html', {'students': students})

def students_edit(request, students_idstudent):
    student = get_object_or_404(Student, idstudent=students_idstudent)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            print(request, 'El student se ha actualizado correctamente.')
            return redirect("student")
        else:
            print(request, 'Hubo un error al actualizar el student.')
            print(form.errors)
    else:
        form = StudentForm(instance=student)
    return render(request, "edit_student.html", {"student": student, "form": form})
