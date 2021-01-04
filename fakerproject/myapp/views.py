from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def view(request):
    s = Student.objects.all().order_by('marks')
    d = {'fake':s}
    return render(request,'html/1.html',d)
