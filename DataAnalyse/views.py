from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from DataAnalyse.models import Twitter
from django.shortcuts import render_to_response, redirect
from DataAnalyse.forms import EventChoose
import json
import convert
import run_idf
import config
from django.template import Context

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
            if request.GET.has_key("draw"):
                # return redirect('test/')
                return test(request)
            if event_form.is_valid():
                cd = event_form.cleaned_data
                if cd["event_list"]:
                    # message = 'You searched for: %r' % cd["event_list"]
                    event = cd["event_list"]
                    # return HttpResponse(event)
                    if request.GET.has_key("generate"):
                        run_algorithm(event)
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

def run_algorithm(event):
    if event == config.event_mh370:
        run_idf.run(start=config.start_mh370, end=config.end_mh370, interval=config.interval_mh370, event=config.event_mh370)
    elif event == config.event_earthquake:
        run_idf.run(start=config.start_earthq, end=config.end_earthq, interval=config.interval_earthq, event=config.event_earthquake)
    elif event == config.event_epl:
        run_idf.run(start=config.start_epl, end=config.end_epl, interval=config.interval_epl, event=config.event_epl)

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
    '''
    array = [
          ['Year', 'Sales'],
          ['2004',  1000],
          ['2005',  1170],
          ['2006',  660],
          ['2007',  1030]
        ]
    print array
    '''
    array = convert.run()

    return render_to_response('DataAnalyse/test.html',
                              {
                                'array': json.dumps(array)
                              })
