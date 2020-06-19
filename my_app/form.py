from django import forms

from .models import Categories, Tasks

class AddCategoryForm(forms.ModelForm):

    class Meta:
        model = Categories
        field = [
            'title',
        ]