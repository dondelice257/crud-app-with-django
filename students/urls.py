from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('dropouts', views.dropouts, name='dropouts'),
    path('students/details/<int:id>', views.students_details, name='students_details'),
    
]
