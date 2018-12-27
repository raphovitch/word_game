from django.contrib import admin
from game_app.models import Category, Word, Game, Result
# , Score


# Register your models here.

admin.site.register(Category)
admin.site.register(Word)
admin.site.register(Game)
admin.site.register(Result)
# admin.site.register(Score)