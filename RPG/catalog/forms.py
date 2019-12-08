from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    
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
    