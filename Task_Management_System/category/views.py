from django.shortcuts import render,redirect
from category.forms import AddCategoryForm

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        add_category_form = AddCategoryForm(request.POST)
        if add_category_form.is_valid():
            print(add_category_form.cleaned_data)
            add_category_form.save()
            return redirect('add_category')
    else:
        add_category_form = AddCategoryForm()
    return render(request,'addCategoryForm.html',{'form':add_category_form})
