from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add-character$', views.add_character, name='add-character'),
    url(r'^character-details/(?P<pk>[0-9]+)$', views.character_details, name='character-details'),
    url(r'^manage-skills/(?P<characterId>[0-9]+)$', views.manage_skills, name='manage-skills'),
    url(r'^assign-skills$', views.assign_skills, name='assign-skills'),
    url(r'^add-skill$', views.add_skill, name='add-skill'),
    url(r'^skill-details/(?P<skill_id>[0-9]+)$', views.skill_details, name='skill-details'),
]