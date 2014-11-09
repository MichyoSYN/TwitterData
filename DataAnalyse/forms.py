__author__ = 'Michyo'

from django import forms

EVENT_CHOICES = (
    ('MH370', 'MH370'),
    ('earthquake', 'Chile Earthquake'),
    ('football', 'Football Game'),
)

class EventChoose(forms.Form):
    event_list = forms.ChoiceField(choices=EVENT_CHOICES)
    event_keyword = forms.CharField()
