from django.urls import path
from . import views

app_name = 'game_app'

urlpatterns = [

	path('game/', views.game_page, name='game_page'),
	path('get_word/', views.get_word, name='get_word'),	
	path('homepage/', views.homepage, name='homepage'),
	path('end_game/', views.end_game, name='end_game'),
	path('highboard/', views.get_high_scores, name='highboard'),		
	
]