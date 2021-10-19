from django.shortcuts import render
from .models import Student

# Create your views here.
def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"home.html")

def saveform(request):
    info=Student.objects.all()
    if request.method=='POST':
        form=Student(name=request.POST['name'],fname=request.POST['fname'],email=request.POST['email'],contact=request.POST['contact'],gender=request.POST['sex'],dob=request.POST['date'])
        form.save()
    return render(request,"studentd.html",{"form_list":info})

def edit(request):
    id=request.GET['id']
    d=Student.objects.filter(id=id)
    return render(request,"edit.html",{"form_list":d})
def editform(request):
    info = Student.objects.all()
    d=Student.objects.filter(id=request.POST['id']).update(name=request.POST['name'],fname=request.POST['fname'],email=request.POST['email'],contact=request.POST['contact'],gender=request.POST['sex'],dob=request.POST['date'])
    return render(request, "studentd.html", {"form_list": info})

def delete(request):
    info = Student.objects.all()
    d = Student.objects.filter(id=request.GET['id']).delete()
    return render(request, "studentd.html", {"form_list": info})