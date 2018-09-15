
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('complete/<int:todo_id>/', views.completeaddTodo, name='complete'),
    path('deletecomplete/', views.deleteComplete, name='deletecomplete'),
    path('deleteall/', views.deleteall, name='deleteall'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
]
