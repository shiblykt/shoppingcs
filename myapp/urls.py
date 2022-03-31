from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('otp/',views.otp,name='otp'),
    path('logout',views.logout,name='logout'),
]