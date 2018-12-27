from django.shortcuts import render
from game_app.models import Category, Word, Result, Game
from profile_app.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def all_games_from_user(request):
	user = request.user
	user_p = UserProfileInfo.objects.get(user = user)
	all_games = Game.objects.filter(user = user_p)
	return render(request, 'all_games_from_user.html', {
			'all_games' : all_games, 
			'logged_in':True,
			'user':user
			})