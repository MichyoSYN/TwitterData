from django.shortcuts import render, get_object_or_404

from DataAnalyse.models import Twitter

# Create your views here.

def index(request):
    latest_twits_list = Twitter.objects.order_by('-pub_date')[:5]
    context = {'latest_data_list': latest_twits_list}
    return render(request, 'polls/index.html', context)

def detail(request, id):
    twit = get_object_or_404(Twitter, pk = id)
    return render(request, 'polls/detail.html', {'twit': twit})
