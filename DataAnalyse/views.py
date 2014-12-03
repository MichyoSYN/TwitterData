from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from DataAnalyse.models import Twitter
from django.shortcuts import render_to_response
from DataAnalyse.forms import EventChoose

# Create your views here.

'''
def test(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
'''

class IndexView(generic.ListView):
    template_name = 'DataAnalyse/index.html'
    context_object_name = 'latest_twits_list'

    '''
    def get_queryset(self):
        # Return the last five published questions.
        return Twitter.objects.order_by('-pub_date')[:5]
    '''

    def get(self, request, *args, **kwargs):
        event = 'Please choose event.'
        if request.method == "GET":
            event_form = EventChoose(request.GET)
            if event_form.is_valid():
                cd = event_form.cleaned_data
                if cd["event_list"]:
                    # message = 'You searched for: %r' % cd["event_list"]
                    event = cd["event_list"]
                    # return HttpResponse(event)
            else:
                event_form = EventChoose()
        # ** Return the latest 5 tweets related with event. **
        latest_twits_list = Twitter.objects.filter(event=event).order_by('-pub_date')[:5]
        return render_to_response('DataAnalyse/index.html',
                                  {
                                      'event_form': event_form,
                                      'latest_twits_list': latest_twits_list,
                                      'event': event
                                  })

class DetailView(generic.DetailView):
    model = Twitter
    template_name = 'DataAnalyse/detail.html'
    context_object_name = 'twit'

def test(request):
    '''
    if request.method == "GET":
        event_form = EventChoose(request.GET)
        if event_form.is_valid():
            cd = event_form.cleaned_data
            if cd["event_list"]:
                message = 'You searched for: %r' % cd["event_list"]
                return HttpResponse(message)
        else:
            event_form = EventChoose()
    return render_to_response('DataAnalyse/test.html', {'event_form': event_form})'''
    return render_to_response('DataAnalyse/test.html')
