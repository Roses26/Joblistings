from django.urls import path

#from .views import home
from employeePage.views import registration, login, logout, dashboard, employee_home, employee_create, employee_update, employee_detail, employee_delete

urlpatterns = [
    path('registration', registration, name='registration'),
    path('dashboard', dashboard, name='dashboard'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('home', employee_home, name='employee_home'),
    path('create', employee_create, name='employee_create'),
    path('update/<int:emp_id>/', employee_update, name='update'),
    path('detail/<int:emp_id>/', employee_detail, name= 'detail'),
    path('delete/<int:emp_id>/', employee_delete, name= 'delete')
] 