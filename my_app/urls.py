from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_category/', views.delete_category, name='delete_category'),
    path('delete_todo/<int:task_id>/', views.delete_todo, name='delete_todo'),
    path('new_search', views.new_search, name='new_search'),
    path('day', views.day, name='day'),
    path('save_changes/', views.save_changes, name='save_changes'),
]