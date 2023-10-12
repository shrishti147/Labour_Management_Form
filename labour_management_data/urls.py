from django . urls import include, path
from . import views

urlpatterns = [
    path('', views.labour_management_data, name='labour_management_data'),
]