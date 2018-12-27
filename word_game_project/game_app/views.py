from django.shortcuts import render
from game_app.models import Category, Word, Result, Game
from profile_app.models import UserProfileInfo
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json


def get_high_scores(request):
	best_games = Game.objects.all().order_by('-result')[:3]
	if request.user.is_authenticated:
		user = request.user
		return render(request, 'highboard.html', context ={
				'logged_in':True,
				'user':user, 
				'best_games':best_games,
			})

	else : 
		return render(request, 'highboard.html', context ={
				'logged_in':False,
				'best_games':best_games,
			})



def homepage(request):
	if request.user.is_authenticated:
		user = request.user
		return render(request, 'homepage.html', context ={
				'logged_in':True,
				'user':user
			})
	else : 
		return render(request, 'homepage.html', context ={
				'logged_in':False,
			})



def get_coded_word(word):

	word_coded = []

	for letter in word:
		if letter == 'a' or letter == 'b' or letter == 'c': 
			number = 2

		elif letter == 'd' or letter == 'e' or letter == 'é' or letter == 'ê' or letter == 'ë' or letter == 'è' or letter == 'f':
			number = 3

		elif letter == 'g' or letter == 'h' or letter == 'i':
			number = 4

		elif letter == 'j' or letter == 'k' or letter == 'l':
			number = 5

		elif letter == 'm' or letter == 'n' or letter == 'o':
			number = 6

		elif letter == 'p' or letter == 'q' or letter == 'r' or letter == 's':
			number = 7

		elif letter == 't' or letter == 'u' or letter == 'v':
			number = 8

		else:
			number = 9

		word_coded.append(number)
	

	return (word_coded)

# Create your views here.

@login_required
def game_page(request):

	user = request.user
	if 'words_used' in request.session: 
		del request.session['words_used']

	return render(request, 'game.html', context ={
			'logged_in':True,
			'user':user
			})
	



def get_word(request):
	if 'words_used' not in request.session: 
		request.session['words_used']=[]
	print(', '.join(request.session['words_used']))
	word_object = Word.objects.exclude(word__in=request.session['words_used']).order_by('?')[0]
	print(word_object)
	category = word_object.category.name
	request.session['words_used'].append(word_object.word)
	word_string = word_object.word.lower()
	list_number_word = get_coded_word(word_string) 
	
	request.session.modified = True
	print(request.session['words_used'])

	coded_word_list = []
	for i in list_number_word:
		coded_word_list.append(str(i))

	coded_word_string = ' '.join(coded_word_list)
	

	word = {
		'word' : word_string,
		'category': category,
	}

	response = {
		'word': word,
		'coded_word': coded_word_string,
		'code' :200,
	}

	return JsonResponse(response)

@login_required
def end_game(request):
	user = request.user
	user_p = UserProfileInfo.objects.get(user = user)
	if request.method == 'POST':
		words_found = json.loads(request.POST.get('words_found'))
		print(words_found)
		print('######')
		score = request.POST.get('score')

		score_int = int(score)
		result = Result.objects.get_or_create(user= user_p, points=score_int)[0]

		game = Game.objects.get_or_create(user= user_p, result= result)[0]

		list_object_words_found = []

		for i in words_found :
			print('#####')
			print(type(i))
			print('#####')
			word_object = Word.objects.get(word=i)
			list_object_words_found.append(word_object)

		for word in list_object_words_found:
			game.words.add(word)

		response = {
			'code':200
		}

		return JsonResponse(response)



	

	
