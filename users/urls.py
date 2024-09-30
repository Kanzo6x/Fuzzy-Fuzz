from django.urls import path
from .views import login_view, signup_view, logout_view, profile_view, previous_orders_view

app_name = 'users'  

urlpatterns = [
    path('login/', login_view, name='login'),  
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('previous_orders/', previous_orders_view, name='previous_orders'),
]
