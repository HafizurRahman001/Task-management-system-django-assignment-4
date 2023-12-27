from django import forms
from task.models import AddTask


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = '__all__'

        widgets= {
            'task_assigned_date': forms.DateInput(attrs={'type':'date'}),
            'task_description':forms.Textarea(attrs={'rows':4})
        }