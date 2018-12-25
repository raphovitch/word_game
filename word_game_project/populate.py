import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'word_game_project.settings')
import django
django.setup()
from game_app.models import Category,Word

def read_word_json():
    with open('words.json', 'r') as f :
        word_list = json.load(f)
    return word_list

def get_words_and_categories():
	words_list = read_word_json()
	for element in words_list:
		category = element['category']
		word = element['word']

		category_object = Category.objects.get_or_create(name=category)[0]
		Word.objects.get_or_create(word=word, category=category_object)[0]


if __name__ == '__main__':
    print('Starting to populate...')
    get_words_and_categories()
    print('Finished populating!')
