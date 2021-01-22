from django.shortcuts import render
from django.http import Http404
from polls.models import Poll

# Create your views here.
def detail(request, poll_id):
	try:
		p = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404("Poll does not exist")
	return render(request, 'polls/detail.html', {'poll': p})