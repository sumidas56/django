from django.shortcuts import render
from .forms import Todoform
from .models import Todo
# Create your views here.

def index(request):
    context={}

    if request.method=='POST':
        if 'submit' in request.POST:
            todo_form=Todoform(request.POST)

            todo_form.save()



    todo=Todo.objects.all()
    todo_form=Todoform()

    
    context['todo_form']=todo_form
    context['todo']=todo

    return render(request,'index.html',context)
