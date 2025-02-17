from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    username = models.CharField(max_length=255)
    authuser = models.OneToOneField(User, on_delete=models.CASCADE)
    userId = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique = True, null = False)
    friends = models.ManyToManyField("self", blank = True)
    def __str__(self):
        return self.username

class Mindmap(models.Model):
    mapid = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique = True, null = False)
    creatorId = models.BigIntegerField(blank=False)
    name = models.CharField(max_length = 120, null = True)
    map = models.TextField()
    viewers = models.ManyToManyField(Member, blank = True)
    def __str__(self):
        return self.name


class Document(models.Model):
    documentId = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique = True, null = False)
    creatorId = models.BigIntegerField(blank=False)
    name = models.CharField(max_length = 120, null=True)
    text = models.TextField()
    viewers = models.ManyToManyField(Member, blank = True)
    Mindmaps = models.ManyToManyField(Mindmap, blank = True, related_name="documents")
    def __str__(self):
        return self.name