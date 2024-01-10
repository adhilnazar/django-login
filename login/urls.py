
from django.urls import path
from . import views
# app_name='login_'

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.log_in,name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    
]