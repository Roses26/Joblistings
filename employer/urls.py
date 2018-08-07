from django.urls import path

#from .views import home
from employer.views import employer_home, employer_create, employer_update, employer_detail, employer_delete

urlpatterns = [
    path('', employer_home, name='employer_home'),
    path('create', employer_create, name='employer_create'),
    path('update/<int:emp_id>/', employer_update, name='update'),
    path('detail/<int:emp_id>/', employer_detail, name= 'detail'),
    path('delete/<int:emp_id>/', employer_delete, name= 'delete')
]