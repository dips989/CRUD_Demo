
from django.urls import path
from crud_app import views

urlpatterns = [
    path('', views.login_form, name="login_form"),
    path('login_ajax/', views.login_ajax, name="login_ajax"),
    path('dashboard_page/', views.dashboard_page, name="dashboard_page"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('save_student_ajax/', views.save_student_ajax, name="save_student_ajax"),
    path('edit_data/', views.edit_data, name="edit_data"),
    path('delete/', views.delete, name='delete'),
]
