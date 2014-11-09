__author__ = 'Michyo'

from django import forms

EVENT_CHOICES = (
    ('1', 'MH370'),
    ('2', 'Earthquake'),
    ('3', 'Football'),
)

class EventChoose(forms.Form):
    event_list = forms.ChoiceField(choices=EVENT_CHOICES)
