from individual_work_2 import views
from django.urls import path

urlpatterns = [
    path('', views.main),
    path('workers_departments/', views.workers_departments),
    path('workers_in_department/<int:id>/', views.workers_in_department),
    path('department_form/', views.department_form),
    path('department_worker_form/', views.department_worker_form),


]