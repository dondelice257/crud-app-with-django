from django.http import HttpResponse
from django.template import loader
from .models import Student
from django.db.models import Q


def students(request):
  students=Student.objects.all().order_by('first_name').values()
  template = loader.get_template('students.html')
  context={
      "students": students
  }
  return HttpResponse(template.render(context, request))

def students_details(request, id):
  student=Student.objects.get(id=id)
  template = loader.get_template('student-details.html')
  context={
      "student": student
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def dropouts(request):
  template = loader.get_template('dropout.html')
  return HttpResponse(template.render())