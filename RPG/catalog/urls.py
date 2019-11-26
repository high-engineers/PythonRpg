from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^addCharacter$', views.addCharacter, name='addCharacter'),
    url(r'^character-details/(?P<pk>[0-9]+)$', views.characterDetails, name='character-details'),
    url(r'^add-skill/(?P<characterId>[0-9]+)$', views.addSkill, name='add-skill')

]