from django.shortcuts import render, redirect

from mainapp.forms import SchoolForm, StudentForm
from mainapp.models import School, Student


def school_view(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show-school')
            except:
                pass
    else:
        form = SchoolForm()

    return render(request, 'index.html', {'form': form})


def show_school(request):
    schools = School.objects.all()
    return render(request, 'show_school.html', {'schools': schools})


def edit_school(request, id):
    school = School.objects.get(id=id)
    return render(request, 'edit_school.html', {'school': school})


def update_school(request, id):
    school = School.objects.get(id=id)
    form = SchoolForm(request.POST, instance=school)
    if form.is_valid():
        form.save()
        return redirect('/show-school')
    return render(request, 'edit-school.html', {'school': school})


def destroy_school(request, id):
    school = School.objects.get(id=id)
    school.delete()
    return redirect('/show-school')

def student_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show-student')
            except:
                pass
    else:
        form = StudentForm()

    return render(request, 'index1.html', {'form': form})


def show_student(request):
    student = Student.objects.all()
    return render(request, 'show_student.html', {'students': student})


def edit_student(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit_student.html', {'student': student})


def update_student(request, id):
    student = Student.objects.get(id=id)
    print(request)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/show-student')
    return render(request, 'edit_student.html', {'student': student})


def destroy_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/show-student')
