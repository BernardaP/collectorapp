from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Paintbrush
from .forms import CanvasForm



# Students data
# class Student:
#   def __init__(self, name, city, age, bio):
#     self.name = name
#     self.city = city
#     self.age = age
#     self.bio = bio

# students = [
#   Student('Lolo', 'Las Vegas', 26, 'I love to draw stuff'),
#   Student('Raven', 'Fargo', 22, 'I love to paint stuff'),
#   Student('Sachi', 'New York ', 44, 'I love to draw and paint stuff'),
# ]



# Create your views here.
# Home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')


# About view
def about(request):
  return render(request, 'about.html')


# All students view
def students_index(request):
  students = Student.objects.all()
  return render(request, 'students/index.html', {'students': students })

# Individual student detail
def student_detail(request, student_id):
  student = Student.objects.get(id=student_id)
  # Get brushes student doesn't have
  paintbrushes_student_doesnt_have = Paintbrush.objects.exclude(id__in = student.paintbrushes.all().values_list('id'))
  canvas_form = CanvasForm()
  return render(request, 'students/detail.html', 
    { 'student': student, 'canvas_form': canvas_form, 'paintbrushes': paintbrushes_student_doesnt_have}
  )

# Post request to update database with FORM input
def add_canvas(request, student_id):
  form = CanvasForm(request.POST)
  # validate form
  if form.is_valid():
    new_canvas = form.save(commit=False)
    new_canvas.student_id = student_id
    new_canvas.save()
  return redirect('detail', student_id=student_id)

 