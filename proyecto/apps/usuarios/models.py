from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class perfil_usuario(models.Model):
	user=models.OneToOneField(User)
	
	def __str__(sefl):
		return str(sefl.user)