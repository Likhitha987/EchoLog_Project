from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # This makes the "Home" page show your list of scraps
    path('', views.scrap_list, name='scrap_list'),
    path('add/', views.add_scrap, name='add_scrap'),
    path('register/', views.register, name='register'),
    path('edit/<int:pk>/', views.edit_scrap, name='edit_scrap'),
    path('logout/', auth_views.LogoutView.as_view(next_page='register'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('delete/<int:pk>/', views.delete_scrap, name='delete_scrap'),
]



    