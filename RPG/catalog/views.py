# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from catalog.models import Character, Entity, Race, Statistics, Condition

def index(request):
    characters_list = Character.objects.all()
    return render(request, 'index.html', {
        'characters_list': characters_list,
    })

def add(request):
    races_list = Race.objects.all()
    
    return render(request, 'add.html', {
        'races_list': races_list
    })

def addCharacter(request):
    strength = request.POST.get('strength')
    intelligence = request.POST.get('intelligence')
    
    statistics = Statistics.objects.create(
        strength = strength,
        dexterity = request.POST.get('dexterity'),
        intelligence = intelligence,
        wisdom = request.POST.get('wisdom'),
        luck = request.POST.get('luck'),
        charisma = request.POST.get('charisma')
    )

    condition = Condition.objects.create(
        health = strength * 2,
        max_health = strength * 2,
        mana = intelligence * 2,
        max_mana = intelligence * 2,
        experience = 0,
        max_experience = 100
    )
    
    race_name = request.POST.get('race')

    race = Race.objects.get(name = race_name)
    
    entity = Entity.objects.create(
        name = request.POST.get('name'),
        age = request.POST.get('age'),
        level = 1,
        quote = request.POST.get('quote'),
        story = request.POST.get('story'),
        sex = request.POST.get('sex'),
        race_id = race.id,
        statistics_id = statistics.id,
        condition_id = condition.id
    )
    return redirect('index')
