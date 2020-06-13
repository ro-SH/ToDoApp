from datetime import datetime
from django.shortcuts import HttpResponseRedirect, render
from .models import Categories, Tasks

DATETIME_FORMAT = '%b %d, %Y %I:%M %p'

def home(request):
    categories = Categories.objects.all()
    context = {
        'category_list': categories,
    }
    return render(request, 'my_app/index.html', context)


def add_todo(request):
    categories = Categories.objects.all()
    context = {
        'category_list': categories,
    }
    try:
        category = Categories.objects.get(pk=request.POST.get('category'))
        to_do = request.POST.get('to_do')
        date = request.POST.get('date')
        time = request.POST.get('time')
        formatted_date = datetime.strptime(date + ' ' + time, DATETIME_FORMAT)
        is_done = False
    except (KeyError, Categories.DoesNotExist):
        context['error_message'] = "You did not select a category."
        return render(request, 'my_app/index.html', context)
    except ValueError:
        context['error_message'] = "Incorrect date or time."
        return render(request, 'my_app/index.html', context)
    
    Tasks.objects.create(title=to_do, deadline=formatted_date, category=category, is_done=False)
    return HttpResponseRedirect('/')


def delete_todo(request, task_id):
    Tasks.objects.get(id=task_id).delete()
    return HttpResponseRedirect('/')