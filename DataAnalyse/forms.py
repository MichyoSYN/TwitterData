__author__ = 'Michyo'

from django import forms

# ** Provide a series of choices to be chosen. **
EVENT_CHOICES = (
    ('MH370', 'MH370'),
    ('earthquake', 'Chile Earthquake'),
    ('epl', 'Football Game'),
)

class EventChoose(forms.Form):
    # ** This is a list of events that can be selected. **
    event_list = forms.ChoiceField(choices=EVENT_CHOICES)
    # event_keyword = forms.CharField()
