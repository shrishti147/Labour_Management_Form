from django . urls import include, path
from . import views

urlpatterns = [
    path('', views.labour_details, name='labour_details'),
    path('/labourdata.html',views.labourdata, name='labourdata'),
    #path('/labourdata.html',views.testing, name='testing'),
]