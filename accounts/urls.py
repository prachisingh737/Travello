from django.urls import path
from .views import login_view, register_view, home_view,  add_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('', home_view, name='home'),
        path('add/', add_view, name='add'),  # Add this line for the 'add' view

]
