from django.urls import path

#from .views import home
from jobs.views import home, create, update, detail, delete

urlpatterns = [
    path('', home, name='home'),
    path('create', create, name='create'),
    path('update/<int:emp_id>/', update, name='update'),
    path('detail/<int:emp_id>/', detail, name= 'detail'),
    path('delete/<int:emp_id>/', delete, name= 'delete')
]
8
