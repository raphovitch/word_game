from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=500, blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

	def __repr__(self):
		return "<User: {}>".format(self.user.username)

	def __str__(self):
		return '{} {}'.format(self.user.first_name, self.user.last_name)