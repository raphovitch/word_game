from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
	path('signup/', views.signup, name='signup'),
	path('login/', views.log_in, name='loginpage'),
	path('logging_out/', views.logging_out, name='logging_out'),
]