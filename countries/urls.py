from django.urls import path
from . import views

urlpatterns = [
path('', views.countries, name='countries'),
path('details/<int:id>', views.detail, name='country-details')

    
    
]
