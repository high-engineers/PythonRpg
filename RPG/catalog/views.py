# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Character
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def index(request):
    character_list = Character.objects.all()
    template = loader.get_template('catalog/index.html')
    context = {
        'character_list': character_list
    }

    return HttpResponse(template.render(context, request))
