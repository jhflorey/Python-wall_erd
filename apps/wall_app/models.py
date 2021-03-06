from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	blog = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

# class User(models.Model):
# 	first_name = models.CharField(max_length=45)
# 	last_name = models.CharField(max_length=45)
# 	# email = models.EmailField()
# 	password = models.CharField(max_length=100)
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	updated_at = models.DateTimeField(auto_now = True)

# class Message(models.Model):
#     message = models.TextField()
#     user = models.ForeignKey(User)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
	comment = models.TextField(max_length=1000)
	blog = models.ForeignKey(Blog)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


