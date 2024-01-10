from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)


class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    team = models.ForeignKey(Team, related_name='members', on_delete=models.SET_NULL, null=True)
