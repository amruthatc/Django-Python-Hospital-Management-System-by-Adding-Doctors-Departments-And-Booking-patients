from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


from .models import Departments,Doctors

# Create your views here.
def index(request):
   
    person = {
             'name': 'John',
             'age': 30,
             'place': 'calicut',
             'num1':10,
             'num2':[1,2,3,4,5,6,7,8,9,10],
             'fruits':['apple','banana','grapes']
            }


    return render(request, 'index.html',person)

def about(request):
     return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def contact(request):
    return render(request,'contact.html')

def department(request):
    return render(request,'department.html')


def department(request):
    dict_dept={
       'dept':Departments.objects.all()

    }
    return render(request,'department.html',dict_dept)