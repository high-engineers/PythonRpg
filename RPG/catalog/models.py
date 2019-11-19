# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Race(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=2048)
    backstory = models.CharField(max_length=2048)
    class Meta:
        db_table = 'Race'

class Statistics(models.Model):
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    inteligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    class Meta:
        db_table = 'Statistics'

class Condition(models.Model):
    health = models.IntegerField(default=0)
    max_health = models.IntegerField(default=0)
    mana = models.IntegerField(default=0)
    max_mana = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    max_experience = models.IntegerField(default=0)
    class Meta:
        db_table = 'Condition'

class Skill(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=2048)
    mana_cost = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    multiplier = models.IntegerField(default=0)
    class Meta:
        db_table = 'Skill'

class Entity(models.Model):
    skills = models.ManyToManyField('Skill')
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    statistics = models.ForeignKey(Statistics, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    level = models.IntegerField(default=1)
    story = models.CharField(max_length=2048)
    quote = models.CharField(max_length=256)
    sex = models.CharField(max_length=8)
    class Meta:
        db_table = 'Entity'

class Npc(Entity, models.Model):
    class Meta:
        db_table = 'Npc'

class Character(Entity, models.Model):
    class Meta:
        db_table = 'Character'
    def __str__(self):
        return 'xd'

class User(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    class Meta:
        db_table = 'User'