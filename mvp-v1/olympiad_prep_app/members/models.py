from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
  username = models.CharField(max_length=255)
  authuser = models.OneToOneField(User, on_delete=models.CASCADE)
  userId = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique = True, null = False)
  friends = models.ManyToManyField("self", null = True)

class Mindmap(models.Model):
    mapid = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique = True, null = False)
    creatorId = models.BigIntegerField(blank=False)
    map = models.TextField()
    viewers = models.ManyToManyField(Member, blank = True)


class Document(models.Model):
    documentId = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique = True, null = False)
    creatorId = models.BigIntegerField(blank=False)
    text = models.TextField()
    viewers = models.ManyToManyField(Member, blank = True)