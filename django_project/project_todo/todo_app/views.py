from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todo_list(request):
    return HttpResponse("This is from todo_list function")