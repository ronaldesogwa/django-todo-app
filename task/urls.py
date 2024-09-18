from django.urls import path

from .views import (DashboardView, task_list, task_add, task_detail, task_edit, task_delete)

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('task/', task_list, name='task_list'),
    path('add/', task_add, name='task_add'),
    path("detail/<int:pk>/", task_detail, name='task_detail'),
    path("edit/<int:pk>/", task_edit, name='task_edit'),
    path("delete/<int:pk>/", task_delete, name='task_delete'),


]