from django.http import HttpResponse
from django.shortcuts import redirect, render

from main.forms import StudentForm
from main.models import Student


def show_all_students(request):
    """
    Shows all students in template
    """
    students = Student.objects.all()
    return render(
        request=request,
        template_name='index.html',
        context={
            'students': students,
        }
    )


def create_student(request):
    """
    Creates student by student's name
    """
    student_name_from_request = request.GET.get('name')

    if not student_name_from_request:
        return HttpResponse('Student name missing')

    student = Student()
    student.name = student_name_from_request
    student.save()
    return HttpResponse('Student {} have been created'.format(student.name))


def create_student_by_form(request):
    """
    Create student by Django Forms
    """
    if request.method == 'GET':
        student_form = StudentForm()
        context = {
            'student_form': student_form,
        }

        return render(request, 'student_form.html', context=context)

    elif request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()

        return redirect('/home/form/')
