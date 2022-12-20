from django.urls import path
from account.views import *

urlpatterns = [
    path("register/" , register_view , name= "register"),
    path("" , login_view , name= "login"),
    path("dashboard/" , dashboard_view , name= "dashboard"),
    path('otp/<uid>/', otp , name = 'otp'),
    path('logout', logoutUser , name='logout' ),
    path('profile/' , ProfileView.as_view(), name='profile')
] 