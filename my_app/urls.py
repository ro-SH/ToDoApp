from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:task_id>/', views.delete_todo, name='delete_todo'),
    path('new_search', views.new_search, name='new_search'),
]