from individual_work import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('job_form/', views.job_form),
    path('jobs/<int:id>/', views.job),
    path('contractor_customer_form/', views.contractor_customer_form),
    path('customer-name/', views.get_customer),

]