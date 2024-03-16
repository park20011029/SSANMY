from django.urls import path    
from users.views import SignUpView, LoginView
from users.views import login_page
urlpatterns = [
    path('',login_page, name='login'),
    path('signup',SignUpView.as_view()),
    path('login', LoginView.as_view()),  
]
 