from django.urls import path

from todos import views

app_name = 'todos'
urlpatterns = [
    path('', views.authenticated, name='authenticated'),
    path('create/', views.create_todo, name='create_todo'),
    path('view/<int:todo_id>/', views.view_todo, name='view_todo')
]
