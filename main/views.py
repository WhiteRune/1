from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View

from main.forms import StudentForm
from main.models import Student


class StudentView(View):

    def get(self, request):
        """
        Show all students in template
        """
        students = Student.objects.all()
        return render(
            request=request,
            template_name='index.html',
            context={
                'students': students,
            }
        )


class StudentCreateView(View):

    def get(self, request):
        """
        Create student by Django Forms
        """
        student_form = StudentForm()
        context = {
            'student_form': student_form,
        }

        return render(request, 'student_form.html', context=context)

    def post(self, request):
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()

        return redirect(reverse('students_list'))


class StudentUpdateView(View):

    def get(self, request, id):
        """
        Create student by Django Forms
        """
        student = get_object_or_404(Student, id=id)

        # генерируем форму
        student_form = StudentForm(instance=student)

        # добавляем форму в контекст
        context = {
            'student_form': student_form,
            'student': student,
        }

        return render(request, 'student_form.html', context=context)

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()

        return redirect(reverse('students_list'))
