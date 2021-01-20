from main.views import StudentView, StudentCreateView, StudentUpdateView
from django.urls import path

urlpatterns = [
    path('', StudentView.as_view(), name='students_list'),
    path('create/', StudentCreateView.as_view(), name='students_create'),
    path('update/', StudentUpdateView.as_view(), name='students_update'),
]
