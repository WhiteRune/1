from django.urls import path

from main.views import create_student, create_student_by_form,\
    show_all_students

urlpatterns = [
    path('', show_all_students, name='students_list'),
    path('create/', create_student, name='students_create'),
    path('form/', create_student_by_form, name='student_form',)
]
