from django import forms
from category.models import AddCategory


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = AddCategory
        fields = '__all__'