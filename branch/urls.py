from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
    path('detail', views.branch_detail, name='branch_detail'),
    path('all', views.branch_all, name='branch_all'),
]