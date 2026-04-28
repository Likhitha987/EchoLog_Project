from django.urls import path
from . import views

urlpatterns = [
    # This makes the "Home" page show your list of scraps
    path('', views.scrap_list, name='scrap_list'),
    path('add/', views.add_scrap, name='add_scrap'),
]