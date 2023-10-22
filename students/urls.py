from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('dropouts', views.dropouts, name='dropouts'),
    path('details/<int:id>', views.students_details, name='students_details'),
    
]
