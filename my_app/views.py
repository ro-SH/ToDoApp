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

def add_category(request):
    category = request.POST.get('category_field')
    Categories.objects.create(title=category)
    return HttpResponseRedirect('/')

def add_todo(request):
    categories = Categories.objects.all()
    context = {
        'category_list': categories,
    }
    try:
        category = Categories.objects.get(title=request.POST.get('category'))
        to_do = request.POST.get('to_do')
        date = request.POST.get('date')
        time = request.POST.get('time')
        formatted_date = datetime.strptime(date + ' ' + time, DATETIME_FORMAT)
    except (KeyError, Categories.DoesNotExist):
        context['error_message'] = "You did not select a category."
        return render(request, 'my_app/index.html', context)
    except ValueError:
        context['error_message'] = "Incorrect date or time format."
        return render(request, 'my_app/index.html', context)
    
    Tasks.objects.create(title=to_do, deadline=formatted_date, category=category, is_done=False)
    return HttpResponseRedirect('/')
    #context['category_scroll_to'] = category
    #HttpResponseRedirect('/')
    #return render(request, 'my_app/index.html', context)
    

def delete_category(request):
    category = request.POST.get('delete_category_list')
    Categories.objects.get(title=category).delete()

    return HttpResponseRedirect('/')

def delete_todo(request, task_id):
    Tasks.objects.get(id=task_id).delete()
    return HttpResponseRedirect('/')

def new_search(request):
    search = request.POST.get('search_field')
    tasks_list = Tasks.objects.filter(title__contains=search)

    if not (tasks_list and search):
        categories = Categories.objects.all()
        context = {
            'category_list': categories,
            'error_message': 'Empty search field.'
        }
        if search:
            context['error_message'] = 'No results for \'' + search + '\'.'
        return render(request, 'my_app/index.html', context)

    context = {
        'search': search,
        'tasks_list': tasks_list,
    }
    return render(request, 'my_app/new_search.html', context)

def day(request):
    categories = Categories.objects.all()
    context = {
        'category_list': categories,
    }
    date = request.POST.get('day_field')
    try:
        datetime.strptime(date, DATETIME_FORMAT[:9])
    except ValueError:
        context['error_message'] = 'Incorrect date format.'
        return render(request, 'my_app/index.html', context)
    
    tasks_list = []
    for task in Tasks.objects.all():
        if task.deadline.strftime(DATETIME_FORMAT).startswith(date):
            tasks_list.append(task)

    if not tasks_list:
        context['error_message'] = 'Not ToDos on \'' + date + '\'.'
        return render(request, 'my_app/index.html', context)

    context = {
        'date': date,
        'tasks_list': tasks_list,
    }
    return render(request, 'my_app/day.html', context)

def save_changes(request):
    for task in Tasks.objects.all():
        print(request.POST.get())
    return HttpResponseRedirect('/')