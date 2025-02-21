from django.db import models
from django.contrib.auth.models import User
from datetime import date
from myadmin.models import *

# Create your models here.

class Profile(models.Model):
	contact = models.BigIntegerField()
	dob = models.DateField()
	gender = models.CharField(max_length=20)
	user = models.OneToOneField(User,on_delete=models.CASCADE)

	class Meta:
		db_table = 'profile'

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Inquiry'

    def __str__(self):
        return self.name

class Feedback(models.Model):
    rating = models.IntegerField() 
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Feedback'

    def __str__(self):
        return f"Feedback from {self.user.username} on {self.date}"
