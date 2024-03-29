from django import forms

class AssignSkillsForm(forms.Form):
    selected_skills = forms.MultipleChoiceField()
    character_id = forms.IntegerField()
    
class AddCharacterForm(forms.Form):
    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    race = forms.ChoiceField(label='Race')
    sex = forms.ChoiceField(label='Sex')
    strength = forms.IntegerField(label='Strength')
    dexterity = forms.IntegerField(label='Dexterity')
    intelligence = forms.IntegerField(label='Intelligence')
    wisdom = forms.IntegerField(label='Wisdom')
    luck = forms.IntegerField(label='Luck')
    charisma = forms.IntegerField(label='Charisma')
    quote = forms.CharField(label='Quote')
    story = forms.CharField(label='Story')

class AddSkillForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    mana_cost = forms.IntegerField()
    damage = forms.IntegerField()
    multiplier = forms.IntegerField()
    