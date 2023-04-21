from Zadanie_po_kursu_2 import views
from django.urls import path

urlpatterns = [
    path('', views.start_page),
    path('reg/', views.registration_page),
    path('log/', views.login_page),
    path('home_page/', views.home_page),
    path('add_money/', views.add_money),
    path('take_money/', views.take_money),

]