from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
import requests

# Create your models here.

class Info(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('info-detail', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
		pk = self.pk 
		super().save(*args, **kwargs)
		print(self.title, self.content, self.date_posted, self.author)
		r = requests.post("http://localhost:5000/reserva/", data={'content': self.content, 'title': self.title, 'date_posted': self.date_posted, 'author': self.author.username})
		print(r.status_code, r.reason)




	
