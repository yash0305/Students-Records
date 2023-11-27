from django.shortcuts import render
from .models import StudentsData

def home(request): 
    return render(request, "home.html") 

# def students(request):
#     form = StudentsData.objects.all()
#     context = {'form':form}
#     return render(request, 'students/home.html', context)
