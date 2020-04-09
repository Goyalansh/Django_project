from django.shortcuts import render
from .models import Topic
# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm


def index(request):
    """the home page for learning"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def new_topic(request):
    """add new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
