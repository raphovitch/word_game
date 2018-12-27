from django.urls import path
from . import views

app_name = 'profile_app'

urlpatterns = [
	# path('edit_profile/', views.edit_page, name='edit_profile'),
	path('all_games_from_user/', views.all_games_from_user, name='all_scores'),
]