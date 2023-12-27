from django.shortcuts import render,redirect
from task.forms import AddTaskForm
from task.models import AddTask

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        add_task_form = AddTaskForm(request.POST)
        if add_task_form.is_valid():
            print(add_task_form.cleaned_data)
            add_task_form.save()
            return redirect('show_task')
    else:
        add_task_form = AddTaskForm()
    return render(request,'addTaskForm.html', {'form':add_task_form})


def edit_task(request,id):
    edited_task = AddTask.objects.get(pk=id)
    add_task_form = AddTaskForm(instance=edited_task)
    if request.method == 'POST':
        add_task_form = AddTaskForm(request.POST,instance=edited_task)
        if add_task_form.is_valid():
            print(add_task_form.cleaned_data)
            add_task_form.save()
            return redirect('show_task')
    return render(request,'addTaskForm.html', {'form':add_task_form})



def show_task(request):
    taskData = AddTask.objects.all()
    return render(request,'displayData.html',{'taskData':taskData})



def delete_task(request,id):
    delete_post = AddTask.objects.get(pk=id)
    delete_post.delete()
    return redirect('show_task')