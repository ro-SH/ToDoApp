from django.shortcuts import render
from .models import Categories, Tasks

# Create your views here.

def home(request):
    categories = Categories.objects.all()
    context = {
        'category_list': categories,
    }
    return render(request, 'my_app/index.html', context)
