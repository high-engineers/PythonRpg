# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .forms import *

from catalog.models import Character, Entity, Race, Statistics, Condition, Skill
from django.db import transaction
import json
def index(request):
    character_list = Entity.objects.all()
    return render(request, 'index.html', {
        'character_list': character_list,
    })

def add_character(request):
    if request.method == "POST":
        print('POST REQUEST')
        form = AddCharacterForm(request.POST)
        print(form.data)
        
        #int vars 
        strength = int(form.data['strength'])
        dexterity = int(form.data['dexterity'])
        intelligence = int(form.data['intelligence'])
        wisdom = int(form.data['wisdom'])
        luck = int(form.data['luck'])
        charisma = int(form.data['charisma'])
        age = int(form.data['age'])
        race_id = form.data['race']

        #str vars
        name = form.data['name']
        story = form.data['story']
        quote = form.data['quote']
        sex = form.data['sex']

        with transaction.atomic():
            print('starting the transaction...')
            print('creating statistics')
            statistics = Statistics.objects.create(
                strength = strength,
                dexterity = dexterity,
                inteligence = intelligence,
                wisdom = wisdom,
                luck = luck,
                charisma = charisma
            )

            print('saving statistics')
            statistics.save()
            print('saving statistics done')
            
            print('creating condition')
            condition = Condition.objects.create(
                health = strength * 2,
                max_health = strength * 2,
                mana = intelligence * 2,
                max_mana = intelligence * 2,
                experience = 0,
                max_experience = 100
            )
            
            print('saving condition')
            condition.save()
            print('saving condition done')

            print('creating character')
            character = Character.objects.create(
                name = name,
                age = age,
                level = 1,
                quote = quote,
                story = story,
                sex = sex,
                race_id = race_id,
                statistics_id = statistics.id,
                condition_id = condition.id
            )
            print('saving character')
            character.save()
            print('saving character done')

            print('transaction commited')
            return redirect('index')
    else:
        print('GET REQUEST')
        races_list = Race.objects.all()
        return render(request, 'add.html', {
            'races_list': races_list
        })
      
def character_details(request, pk):
    entity = Entity.objects.get(id = pk)
    race = Race.objects.get(id = entity.race_id)
    condition = Condition.objects.get(id = entity.condition_id)
    statistics = Statistics.objects.get(id = entity.statistics_id)
    skills = entity.skills.all()
    return render(request, 'character-details.html', {
        'character': entity,
        'race': race,
        'condition': condition,
        'statistics': statistics,
        'skills': skills
    })
    
def manage_skills(request, characterId):
    character = Entity.objects.get(id=characterId)

    skills = list(Skill.objects.all())
    print('\nAll skills: ')
    print(skills)

    character_skills = character.skills.all()
    print('\nCharacter skills')
    print(character_skills)

    print('Available skills:')
    available_skills = list(Skill.objects.exclude(id__in=character_skills))
    print(available_skills)
    
    return render(request, 'manage-skills.html', {
        'available_skills': available_skills,
        'character_skills': character_skills,
        'character_id': characterId
    })

def assign_skills(request):
    print('assign skills here')
    
    if request.method == 'POST':
        form = AssignSkillsForm(request.POST)
        print(form.data)
        selected_skills = form.data["selected_skills"]
        print(selected_skills)
        print(type(selected_skills))
        selected_skills = list(map(int, json.loads(selected_skills)))
        print(type(selected_skills))
        character_id = form.data["character_id"]
        character = Entity.objects.get(id=character_id)
        with transaction.atomic():
            character.skills.clear()
            new_skills = Skill.objects.filter(id__in=selected_skills)
            print(new_skills)   
            character.skills.set(new_skills)
            character.save()
        return redirect("character-details", character_id)
    return redirect("index")

def add_skill(request):
    if request.method == "POST":
        print("POST REQUEST")
        form = AddSkillForm(request.POST)
        print(form.data)

        #int vars
        mana_cost = int(form.data["mana_cost"])
        damage = int(form.data["damage"])
        multiplier = int(form.data["multiplier"])

        #str vars
        name = form.data["name"]
        description = form.data["description"]

        print("Creating skill")
        skill = Skill.objects.create(
            name = name,
            description = description,
            mana_cost = mana_cost,
            damage = damage,
            multiplier = multiplier
        )
        print("saving skill")
        skill.save()
        print("saving skill done")
        return redirect("add-skill")
    else:
        print("GET REQUEST")
        return render(request, "add-skill.html")
        
      

    