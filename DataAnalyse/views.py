from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from DataAnalyse.models import Twitter
from django.shortcuts import render_to_response

# Create your views here.

def test(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

class IndexView(generic.ListView):
    template_name = 'DataAnalyse/index.html'
    context_object_name = 'latest_twits_list'

    def get_queryset(self):
        # Return the last five published questions.
        return Twitter.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Twitter
    template_name = 'DataAnalyse/detail.html'
    context_object_name =  'twit'