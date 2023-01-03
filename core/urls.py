from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='list'),
    path('add/', views.add_taks, name='add'),
    path('details/<id>', views.details_task, name='details'),
    path('update/<id>', views.update_task, name='update'),
    path('complete/<id>', views.complete_task, name='complete'),
    path('delete/<id>', views.delete_task, name='delete'),
    path('accounts/login/', views.login_hendler, name='login'),
    path('accounts/logout/', views.logout_hendler, name='logout'),
    path('accounts/signup/', views.signup_hendler, name='signup'),
]