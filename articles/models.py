from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
	"""docstring for Article"""
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	tumb = models.ImageField(default = 'default.png', blank = True)
	author = models.ForeignKey(User, default=None, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.title

	def snippet(self):
		if len(self.body) > 100:
			return self.body[:100] + "..."
		else:
			return self.bod