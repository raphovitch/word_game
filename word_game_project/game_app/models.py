from django.db import models
from django.contrib.auth.models import User
from profile_app.models import UserProfileInfo

# Create your models here.

class Category(models.Model):
	name = models.TextField(max_length=500)

	def __repr__(self):
		return "<Category: {}>".format(self.name)

	def __str__(self):
		return '{}'.format(self.name)





class Word(models.Model):
	word = models.TextField(max_length=500)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __repr__(self):
		return "<Word: {}>".format(self.word)

	def __str__(self):
		return '{}'.format(self.word)





class Result(models.Model):
	user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
	points = models.IntegerField(default=0)

	def __repr__(self):
		return "<User: {}; Points: {} >".format(self.user.user.username, self.points)

	def __str__(self):
		return 'User: {}; Points: {} >'.format(self.user.user.username, self.points)





class Score(models.Model):
	result_1 = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='result_1')
	result_2 = models.ForeignKey(Result, on_delete=models.CASCADE,related_name='result_2', blank= True)
	result_3 = models.ForeignKey(Result, on_delete=models.CASCADE,related_name='result_3', blank= True)
	result_4 = models.ForeignKey(Result, on_delete=models.CASCADE,related_name='result_4', blank= True)

	def __repr__(self):
		return "<User: {}; Points: {}; User: {}; Points: {} ; User: {}; Points: {} ; User: {}; Points: {}>".format(self.result_1.user.user.username, self.result_1.points,self.result_2.user.user.username, self.result_2.points, self.result_3.user.user.username, self.result_3.points, self.result_4.user.user.username, self.result_4.points)

	def __str__(self):
		return '<User: {}; Points: {}; User: {}; Points: {} ; User: {}; Points: {} ; User: {}; Points: {}>'.format(self.result_1.user.user.username, self.result_1.points,self.result_2.user.user.username, self.result_2.points, self.result_3.user.user.username, self.result_3.points, self.result_4.user.user.username, self.result_4.points)





class Game(models.Model):
	nb_players = models.IntegerField()
	users = models.ManyToManyField(UserProfileInfo, related_name='users')
	words = models.ManyToManyField(Word, related_name='words')
	scores = models.ForeignKey(Score, on_delete=models.CASCADE)
	winner = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)

	def __repr__(self):
		return "<Game n°{}>".format(self.id)

	def __str__(self):
		return 'Game n° {}'.format(self.id)


