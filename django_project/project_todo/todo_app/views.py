from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Todo_app # model.py from 

# Create your views here.
def todo_list(request):
    all_data = {'todo_list' : Todo_app.objects.all()}
    return render(request,'todo_app/todo.html',all_data)


def insert_todo(request:HttpRequest):
    todo = Todo_app(content = request.POST['content'])
    todo.save()
    return redirect('/todo/list')

def delete_todo_item(request,todo_id):
    delete_id = Todo_app.objects.get(id=todo_id)
    delete_id.delete()
    return redirect('/todo/list')