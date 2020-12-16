from django.http import HttpResponse
from django.shortcuts import render
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
