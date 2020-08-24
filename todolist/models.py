from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserToDo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	listitem = models.TextField(max_length=1000)
	date_updated = models.DateTimeField(auto_now=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.listitem[:10])