from django.shortcuts import render
from game_app.models import Category, Word
from django.http import JsonResponse

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


def game_page(request):
	del request.session['words_used']
	return render(request,'game.html')


def get_word(request):
	if request.session.get('words_used', False) == False: 
		request.session['words_used']=[]

	word_object = Word.objects.order_by('?')[0]
	category = word_object.category.name
	word_string = word_object.word.lower()
	list_number_word = get_coded_word(word_string) 
	request.session['words_used'].append(word_string)
	request.session.modified = True
	print(request.session['words_used'])

	coded_word_list = []
	for i in list_number_word:
		coded_word_list.append(str(i))

	coded_word_string = ' '.join(coded_word_list)
	print(coded_word_string)

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



	

	
