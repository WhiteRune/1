from main.views import show_all_students, create_student, \
    create_student_by_form
from django.urls import path

urlpatterns = [
    path('', show_all_students, name='students_list'),
    path('create/', create_student, name='students_create'),
    path('form/', create_student_by_form, name='student_form',)
]
